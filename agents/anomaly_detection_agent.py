import pandas as pd
import numpy as np

class AnomalyDetectionAgent:
    """
    Detects anomalies in trading data using statistical z-scores.
    This version includes sentiment anomaly detection.
    """
    def __init__(self, volume_threshold=3, price_threshold=3, sentiment_threshold=2):
        self.volume_threshold = volume_threshold
        self.price_threshold = price_threshold
        self.sentiment_threshold = sentiment_threshold

    def detect(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()

        # Volume anomalies: detect sudden spikes
        df["volume_zscore"] = (df["volume"] - df["volume"].mean()) / df["volume"].std(ddof=0)
        df["volume_anomaly"] = df["volume_zscore"].abs() > self.volume_threshold

        # Price anomalies: detect sudden jumps/drops
        df["price_return"] = df["price"].pct_change().fillna(0)
        df["price_zscore"] = (df["price_return"] - df["price_return"].mean()) / df["price_return"].std(ddof=0)
        df["price_anomaly"] = df["price_zscore"].abs() > self.price_threshold

        # Sentiment anomalies: detect significant shifts in sentiment
        df["sentiment_zscore"] = (df["sentiment_score"] - df["sentiment_score"].mean()) / df["sentiment_score"].std(ddof=0)
        df["sentiment_anomaly"] = df["sentiment_zscore"].abs() > self.sentiment_threshold

        # Combine all anomalies into a single flag for easy filtering
        df['total_anomaly'] = df['volume_anomaly'] | df['price_anomaly'] | df['sentiment_anomaly']

        return df

