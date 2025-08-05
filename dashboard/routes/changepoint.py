from flask import Blueprint, jsonify
import arviz as az
import pandas as pd
from pathlib import Path
import numpy as np

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
