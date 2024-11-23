import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

class DataCollector:
    def __init__(self, symbols):
        self.symbols = symbols
    
    def get_historical_data(self, start_date, end_date):
        """Collect historical stock data"""
        data = {}
        for symbol in self.symbols:
            ticker = yf.Ticker(symbol)
            data[symbol] = ticker.history(start=start_date, end=end_date)
        return data
    
    def get_realtime_data(self):
        """Collect real-time stock data"""
        data = {}
        for symbol in self.symbols:
            ticker = yf.Ticker(symbol)
            data[symbol] = ticker.info
        return data