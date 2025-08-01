# src/data_loader.py

import pandas as pd
import matplotlib.pyplot as plt

def load_and_clean_data(filepath: str) -> pd.DataFrame:
    """
    Loads Brent oil price data, parses dates, and sorts by date.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Cleaned DataFrame with Date and Price columns.
    """
    df = pd.read_csv(filepath)
    #df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y')
    df['Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=True, errors='coerce')

    df = df.sort_values('Date')
    return df

def plot_price_trend(df: pd.DataFrame) -> None:
    """
    Plots Brent oil price trend over time.

    Args:
        df (pd.DataFrame): DataFrame with Date and Price columns.
    """
    plt.figure(figsize=(14, 6))
    plt.plot(df['Date'], df['Price'], color='navy', linewidth=1.5)
    plt.title("Brent Oil Prices (1987–2022)", fontsize=14)
    plt.xlabel("Date")
    plt.ylabel("Price (USD per barrel)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
