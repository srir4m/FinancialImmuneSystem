import matplotlib.pyplot as plt
import pandas as pd

class VisualizationAgent:
    """
    Plots the trading data, including price, volume, and detected anomalies.
    """
    def plot_trades(self, df: pd.DataFrame):
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

        # Plot 1: Price and trades
        ax1.plot(df.index, df["price"], label="Price", color="black", linewidth=1)
        
        # Highlight price anomalies (blue X)
        price_anoms = df[df["price_anomaly"]]
        ax1.scatter(price_anoms.index, price_anoms["price"],
                    color="blue", marker="x", s=100, label="Price Anomaly")

        # Highlight volume anomalies (red circles)
        vol_anoms = df[df["volume_anomaly"]]
        ax1.scatter(vol_anoms.index, vol_anoms["price"],
                    color="red", marker="o", s=80, alpha=0.8, label="Volume Anomaly")

        # Plot all other normal trades (green dots)
        normal_trades = df[~df['total_anomaly']]
        ax1.scatter(normal_trades.index, normal_trades['price'],
                    color='green', marker='.', s=30, alpha=0.6, label='Normal Trade')

        ax1.set_ylabel("Price")
        ax1.legend()
        ax1.set_title("Trading Activity with Price & Volume Anomalies")
        ax1.grid(True)

        # Plot 2: Sentiment score
        ax2.plot(df.index, df["sentiment_score"], label="Sentiment Score", color="purple", linewidth=1)
        
        # Highlight sentiment anomalies (orange diamonds)
        sentiment_anoms = df[df["sentiment_anomaly"]]
        ax2.scatter(sentiment_anoms.index, sentiment_anoms["sentiment_score"],
                    color="orange", marker="d", s=100, label="Sentiment Anomaly")

        ax2.set_xlabel("Time")
        ax2.set_ylabel("Sentiment Score")
        ax2.legend()
        ax2.set_title("Simulated Market Sentiment")
        ax2.grid(True)

        plt.tight_layout()
        plt.show()

