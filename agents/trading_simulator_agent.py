import random
import pandas as pd
from datetime import datetime, timedelta

class TradingSimulatorAgent:
    """
    Generates synthetic trading data with intentional price and volume anomalies.
    """
    def run(self, num_trades=100, num_anomalies=3):
        trades = []
        ts = datetime.now()
        price = 100
        for i in range(num_trades):
            # Normal trading activity
            price += random.gauss(0, 0.5)
            volume = max(1, int(random.gauss(50, 10)))

            # Insert intentional anomalies at specific points
            if i in random.sample(range(num_trades), num_anomalies):
                # Introduce a significant volume spike
                volume = int(random.gauss(200, 20))
                # Introduce a significant price drop or spike
                price += random.gauss(0, 5)

            trades.append({
                "timestamp": ts + timedelta(minutes=i),
                "price": price,
                "volume": volume
            })
        return trades

