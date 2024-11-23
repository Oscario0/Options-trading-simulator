from config import *
from models.black_scholes import BlackScholes
from data.data_collector import DataCollector
from strategy.sample_strategy import OptionsStrategy
from analysis.performance_metrics import PerformanceAnalyzer

def main():
    # Initialize components
    bs_model = BlackScholes()
    data_collector = DataCollector(STOCKS_TO_TRACK)
    strategy = OptionsStrategy(bs_model, TRADING_THRESHOLD)
    analyzer = PerformanceAnalyzer()
    
    # Collect historical data for backtesting
    historical_data = data_collector.get_historical_data(
        BACKTEST_START_DATE,
        BACKTEST_END_DATE
    )
    
    # Run backtest
    trades = []
    for symbol, data in historical_data.items():
        for date, row in data.iterrows():
            # Calculate theoretical price
            theoretical_price = bs_model.calculate_call(
                S=row['Close'],
                K=row['Close'],  # ATM options
                T=1/12,  # 1 month to expiration
                r=0.02,  # Risk-free rate
                sigma=row['Close'].pct_change().std() * np.sqrt(252)
            )
            
            # Get trading signal
            signal = strategy.analyze_opportunity(
                row['Close'],
                theoretical_price
            )
            
            if signal != "HOLD":
                strategy.execute_trade(signal, symbol, row['Close'], 100)
                trades.append({
                    'date': date,
                    'symbol': symbol,
                    'signal': signal,
                    'price': row['Close'],
                    'theoretical_price': theoretical_price
                })
    
    # Analyze performance
    trades_df = pd.DataFrame(trades)
    performance_metrics = analyzer.calculate_metrics(trades_df)
    
    print("Performance Metrics:")
    for metric, value in performance_metrics.items():
        print(f"{metric}: {value}")

if __name__ == "__main__":
    main()