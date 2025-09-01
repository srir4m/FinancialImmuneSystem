import pandas as pd

class ResponseAgent:
    """
    A simple agent that simulates an automated response to detected anomalies.
    In a real system, this would trigger alerts,
    automated trading responses, or other actions.
    """
    def respond(self, df: pd.DataFrame):
        anomalies = df[df['total_anomaly']]
        if not anomalies.empty:
            print("--- ANOMALY ALERT ---")
            for index, row in anomalies.iterrows():
                anomaly_type = []
                if row['volume_anomaly']:
                    anomaly_type.append("Volume Anomaly")
                if row['price_anomaly']:
                    anomaly_type.append("Price Anomaly")
                if row['sentiment_anomaly']:
                    anomaly_type.append("Sentiment Anomaly")
                
                print(f"Timestamp: {index.strftime('%Y-%m-%d %H:%M')}")
                print(f"  - Detected: {', '.join(anomaly_type)}")
                print(f"  - Price: ${row['price']:.2f}, Volume: {row['volume']}")
                print(f"  - Sentiment Score: {row['sentiment_score']:.2f}")
                print("---")
        else:
            print("No anomalies detected. Financial system stable.")

