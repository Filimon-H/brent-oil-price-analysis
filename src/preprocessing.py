# src/preprocessing.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

def compute_log_returns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Computes log returns from a price time series.

    Args:
        df (pd.DataFrame): DataFrame with 'Price' column.

    Returns:
        pd.DataFrame: DataFrame with an added 'LogReturn' column.
    """
    df = df.copy()
    df['LogReturn'] = np.log(df['Price'] / df['Price'].shift(1))
    return df.dropna()

def plot_log_returns(df: pd.DataFrame) -> None:
    """
    Plots log returns over time.

    Args:
        df (pd.DataFrame): DataFrame with 'Date' and 'LogReturn' columns.
    """
    plt.figure(figsize=(14, 6))
    plt.plot(df['Date'], df['LogReturn'], color='darkgreen', linewidth=1)
    plt.title("Brent Oil Log Returns", fontsize=14)
    plt.xlabel("Date")
    plt.ylabel("Log Return")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def test_stationarity(series: pd.Series, name: str = "Series") -> None:
    """
    Performs Augmented Dickey-Fuller test for stationarity.

    Args:
        series (pd.Series): Time series to test.
        name (str): Name of the series (for printout).
    """
    result = adfuller(series.dropna())
    print(f"ADF Test for {name}:")
    print(f"  Test Statistic = {result[0]:.4f}")
    print(f"  p-value = {result[1]:.4f}")
    print(f"  Stationary: {'Yes' if result[1] < 0.05 else 'No'}\n")
