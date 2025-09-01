import yaml
from agents.trading_simulator_agent import TradingSimulatorAgent
from agents.data_agent import DataAgent
from agents.anomaly_detection_agent import AnomalyDetectionAgent
from agents.visualization_agent import VisualizationAgent
from agents.sentiment_analysis_agent import SentimentAnalysisAgent
from agents.response_agent import ResponseAgent

if __name__ == "__main__":
    # Load config for thresholds and parameters
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    print(config)
    #exit()

    num_trades = config["simulation"]["num_trades"]
    vol_th = config["anomaly_detection"]["volume_threshold"]
    price_th = config["anomaly_detection"]["price_threshold"]
    sentiment_th = config["anomaly_detection"]["sentiment_threshold"]

    # 1. Simulate trades with intentional anomalies
    sim_agent = TradingSimulatorAgent()
    trades = sim_agent.run(num_trades=num_trades, num_anomalies=5)

    # 2. Add sentiment data to the trades (simulated)
    sentiment_agent = SentimentAnalysisAgent()
    trades_with_sentiment = sentiment_agent.run(trades)

    # 3. Collect and preprocess data into a DataFrame
    data_agent = DataAgent()
    df = data_agent.collect(trades_with_sentiment)

    # 4. Detect anomalies based on price, volume, and sentiment
    anomaly_agent = AnomalyDetectionAgent(
        volume_threshold=vol_th,
        price_threshold=price_th,
        sentiment_threshold=sentiment_th
    )
    df = anomaly_agent.detect(df)

    # 5. Take action based on detected anomalies (simple prototype)
    response_agent = ResponseAgent()
    response_agent.respond(df)

    # 6. Visualize the results including the new sentiment data
    viz_agent = VisualizationAgent()
    viz_agent.plot_trades(df)

