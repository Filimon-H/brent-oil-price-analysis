import pandas as pd
from datetime import datetime

def find_closest_event(change_date: pd.Timestamp, events_df: pd.DataFrame) -> pd.Series:
    """
    Finds the event in events_df closest to a given change point date.

    Args:
        change_date (pd.Timestamp): Date of detected change point
        events_df (pd.DataFrame): Event dataset with start_date

    Returns:
        pd.Series: Closest event row
    """
    events_df = events_df.copy()
    events_df["days_diff"] = abs(events_df["start_date"] - change_date)
    return events_df.sort_values("days_diff").iloc[0]

def summarize_model_impact(trace, change_date: pd.Timestamp, closest_event: pd.Series) -> str:
    """
    Summarizes model parameter changes and matched event.

    Args:
        trace (arviz.InferenceData): PyMC3 posterior trace
        change_date (pd.Timestamp): Detected change point date
        closest_event (pd.Series): Closest event info

    Returns:
        str: Human-readable summary of the detected impact
    """
    mu1 = trace.posterior["mu1"].mean().values.item()
    mu2 = trace.posterior["mu2"].mean().values.item()
    sigma1 = trace.posterior["sigma1"].mean().values.item()
    sigma2 = trace.posterior["sigma2"].mean().values.item()

    summary = f"""
Change Point Date: {change_date.date()}
Matched Event: {closest_event['event']} ({closest_event['start_date'].date()})

Mean Return Shift:
  Before: {mu1:.5f}
  After:  {mu2:.5f}
  ΔMean:  {mu2 - mu1:.5f}

Volatility Shift (σ):
  Before: {sigma1:.5f}
  After:  {sigma2:.5f}
  ΔSigma: {sigma2 - sigma1:.5f}
"""
    return summary
