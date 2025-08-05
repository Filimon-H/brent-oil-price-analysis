from flask import Blueprint, jsonify
import arviz as az
import pandas as pd
from pathlib import Path
import numpy as np
import os
from flask import request


# 🔧 Define BASE_DIR as the root of your project
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

changepoint_bp = Blueprint("changepoint", __name__)



# Load data and model outputs
trace_path = Path("../results/metrics/bayesian_trace.nc")

events_path = Path("../data/key_events.csv")
price_path = Path("../data/BrentOilPrices.csv")

trace = az.from_netcdf(trace_path)
df = pd.read_csv(price_path, parse_dates=["Date"])
events_df = pd.read_csv(events_path, parse_dates=["start", "end"])

# Preprocess
df["LogReturn"] = (df["Price"] / df["Price"].shift(1)).apply(np.log)
df.dropna(inplace=True)

# Get changepoint
tau = int(trace.posterior["tau"].mean().values)
change_date = df["Date"].iloc[tau]

@changepoint_bp.route("/summary", methods=["GET"])
def get_summary():
    mu1 = trace.posterior["mu1"].mean().values.item()
    mu2 = trace.posterior["mu2"].mean().values.item()
    sigma1 = trace.posterior["sigma1"].mean().values.item()
    sigma2 = trace.posterior["sigma2"].mean().values.item()

    return jsonify({
        "change_point_index": tau,
        "change_point_date": str(change_date.date()),
        "mu_before": mu1,
        "mu_after": mu2,
        "sigma_before": sigma1,
        "sigma_after": sigma2,
        "delta_mu": mu2 - mu1,
        "delta_sigma": sigma2 - sigma1
    })

@changepoint_bp.route("/events", methods=["GET"])
def get_events():
    return jsonify(events_df.to_dict(orient="records"))


#@changepoint_bp.route("/events/price_trend")
#def price_trend():
    df = pd.read_csv(os.path.join(BASE_DIR, "data", "BrentOilPrices.csv"))
    df['Date'] = pd.to_datetime(df['Date'])
    df = df[df['Date'] >= '2000-01-01']  # Optional filter
    return jsonify({
        "dates": df['Date'].dt.strftime('%Y-%m-%d').tolist(),
        "prices": df['Price'].round(2).tolist()
    })


@changepoint_bp.route("/events/volatility")
def volatility():
    df = pd.read_csv(os.path.join(BASE_DIR, "data", "BrentOilPrices.csv"))
    df["Date"] = pd.to_datetime(df["Date"])
    df["LogReturn"] = np.log(df["Price"] / df["Price"].shift(1))
    df["Volatility"] = df["LogReturn"].rolling(window=30).std()

    df = df.dropna()  # drop rows with NaNs from rolling std

    return jsonify({
        "dates": df["Date"].dt.strftime('%Y-%m-%d').tolist(),
        "volatility": df["Volatility"].round(5).tolist()
    })


#@changepoint_bp.route("/events/price_trend")
#def price_trend():
    df = pd.read_csv(os.path.join(BASE_DIR, "data", "BrentOilPrices.csv"))
    df['Date'] = pd.to_datetime(df['Date'])

    # 🔁 Optional query filters
    start = request.args.get("start_date")
    end = request.args.get("end_date")

    if start:
        df = df[df['Date'] >= pd.to_datetime(start)]
    if end:
        df = df[df['Date'] <= pd.to_datetime(end)]

    return jsonify({
        "dates": df['Date'].dt.strftime('%Y-%m-%d').tolist(),
        "prices": df['Price'].round(2).tolist()
    })


@changepoint_bp.route("/events/price_trend")
def price_trend():
    start_date = request.args.get("start_date", "2000-01-01")
    end_date = request.args.get("end_date", "2022-12-31")
    include_events = request.args.get("include_events", "false").lower() == "true"

    df = pd.read_csv(os.path.join(BASE_DIR, "data", "BrentOilPrices.csv"))
    df["Date"] = pd.to_datetime(df["Date"])
    df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

    response = {
        "dates": df["Date"].dt.strftime("%Y-%m-%d").tolist(),
        "prices": df["Price"].round(2).tolist(),
    }

    if include_events:
        events_df = pd.read_csv(os.path.join(BASE_DIR, "data", "key_events.csv"))
        events_df["start"] = pd.to_datetime(events_df["start"])
        filtered_events = events_df[
            (events_df["start"] >= start_date) & (events_df["start"] <= end_date)
        ]

        # 🔁 Map event dates to price values
        price_lookup = df.set_index("Date")["Price"]

        response["events"] = []
        for _, row in filtered_events.iterrows():
            event_date = row["start"]
            price_on_event = price_lookup.get(event_date, None)
            if pd.notna(price_on_event):
                response["events"].append({
                    "date": event_date.strftime("%Y-%m-%d"),
                    "label": row["event"][:25],  # Optional: show more characters
                    "y": round(price_on_event, 2),
                    "category": row.get("category", "")
                })

    return jsonify(response)



@changepoint_bp.route("/events/price_change_impact")
def price_change_impact():
    window = 7  # days before and after
    price_df = pd.read_csv(os.path.join(BASE_DIR, "data", "BrentOilPrices.csv"))
    price_df["Date"] = pd.to_datetime(price_df["Date"])
    price_df.set_index("Date", inplace=True)

    events_df = pd.read_csv(os.path.join(BASE_DIR, "data", "key_events.csv"))
    events_df["start"] = pd.to_datetime(events_df["start"])

    results = []

    for _, row in events_df.iterrows():
        event_date = row["start"]
        name = row["event"]
        category = row.get("category", "")

        try:
            before = price_df.loc[event_date - pd.Timedelta(days=window): event_date - pd.Timedelta(days=1)]
            after = price_df.loc[event_date + pd.Timedelta(days=1): event_date + pd.Timedelta(days=window)]

            avg_before = before["Price"].mean()
            avg_after = after["Price"].mean()

            if pd.notna(avg_before) and pd.notna(avg_after):
                pct_change = round(((avg_after - avg_before) / avg_before) * 100, 2)
                results.append({
                    "event": name[:50],
                    "date": event_date.strftime("%Y-%m-%d"),
                    "category": category,
                    "avg_before": round(avg_before, 2),
                    "avg_after": round(avg_after, 2),
                    "pct_change": pct_change
                })
        except:
            continue

    return jsonify(results)
