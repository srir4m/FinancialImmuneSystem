import pandas as pd

class DataAgent:
    """
    Collects and processes raw trade data into a structured DataFrame.
    """
    def collect(self, trades):
        # Create a DataFrame from the list of trade dictionaries
        df = pd.DataFrame(trades)
        # Ensure the timestamp is a datetime object and set as index
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.set_index('timestamp')
        return df

