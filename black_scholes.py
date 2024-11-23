import numpy as np
from scipy.stats import norm

class BlackScholes:
    def __init__(self):
        self.N = norm.cdf

    def calculate_call(self, S, K, T, r, sigma):
        """
        Calculate European Call Option Price
        S: Stock price
        K: Strike price
        T: Time to maturity (in years)
        r: Risk-free rate
        sigma: Volatility
        """
        d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
        d2 = d1 - sigma*np.sqrt(T)
        
        call = S*self.N(d1) - K*np.exp(-r*T)*self.N(d2)
        return call

    def calculate_put(self, S, K, T, r, sigma):
        """Calculate European Put Option Price using put-call parity"""
        call = self.calculate_call(S, K, T, r, sigma)
        put = call - S + K*np.exp(-r*T)
        return put