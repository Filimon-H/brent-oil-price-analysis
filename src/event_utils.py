# src/event_utils.py

import pandas as pd
import matplotlib.pyplot as plt


def load_event_data(filepath: str) -> pd.DataFrame:
    """
    Load event data with correct date parsing and rename columns for consistency.

    Args:
        filepath (str): Path to the CSV.

    Returns:
        pd.DataFrame: Cleaned events DataFrame with standard column names.
    """
    df = pd.read_csv(filepath, parse_dates=["start", "end"])
    df = df.rename(columns={"event": "event_name", "start": "start_date", "end": "end_date"})
    return df

def plot_events_on_price(df_prices: pd.DataFrame, df_events: pd.DataFrame) -> None:
    """
    Plot oil prices over time with vertical lines for key events.

    Args:
        df_prices (pd.DataFrame): Brent oil prices (Date, Price)
        df_events (pd.DataFrame): Events with 'start_date' and 'event_name'
    """
    plt.figure(figsize=(14, 6))
    plt.plot(df_prices['Date'], df_prices['Price'], label='Brent Price', color='steelblue')

    for _, row in df_events.iterrows():
        plt.axvline(x=row['start_date'], color='red', linestyle='--', alpha=0.7)
        plt.text(row['start_date'], df_prices['Price'].max()*0.95, 
                 row['event_name'], rotation=90, fontsize=8, color='darkred')

    plt.title("Brent Oil Prices with Key Events Overlay", fontsize=14)
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
