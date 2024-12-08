import pandas as pd
import numpy as np

class PerformanceAnalyzer:
    def __init__(self):
        self.metrics = {}
    
    def calculate_sharpe_ratio(self, returns, risk_free_rate=0.02):
        """Calculate Sharpe Ratio"""
        excess_returns = returns - risk_free_rate
        return np.mean(excess_returns) / np.std(excess_returns) * np.sqrt(252)
    
    def calculate_metrics(self, trades_df):
        """Calculate various performance metrics"""
        self.metrics['total_trades'] = len(trades_df)
        self.metrics['profit_loss'] = trades_df['pnl'].sum()
        self.metrics['win_rate'] = len(trades_df[trades_df['pnl'] > 0]) / len(trades_df)
        self.metrics['volatility'] = trades_df['pnl'].std()
        
        returns = trades_df['pnl'].pct_change().dropna()
        self.metrics['sharpe_ratio'] = self.calculate_sharpe_ratio(returns)
        
        return self.metrics
