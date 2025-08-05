from flask import Blueprint, jsonify
import arviz as az
import pandas as pd
from pathlib import Path
import numpy as np
import os


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


@changepoint_bp.route("/events/price_trend")
def price_trend():
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
