import random  # For generating random numbers
import pandas as pd  # For handling data
def fetch_real_returns(ticker, period='1y'):
    import yfinance as yf
    # Download historical data for the given ticker
    data = yf.download(ticker, period=period)
    # Calculate daily returns from 'Close' prices
    data['Return'] = data['Close'].pct_change()
    # Drop missing values
    returns = data['Return'].dropna()
    return returns, data

# --- Fetch real-world data ---
ticker = 'NVDA'  # Example: Nvidia
returns, data = fetch_real_returns(ticker)

# Calculate mean and std deviation of real returns
mean_return = returns.mean()
std_return = returns.std()

# Use the latest real closing price as the starting price
start_price = data['Close'].iloc[-1]
# Number of days to simulate
days = 30
# Number of simulations to run
simulations = 1000
ending_prices = []

for sim in range(simulations):
    price = start_price
    for day in range(days):
        # Use real mean and std dev for daily return
        daily_return = random.gauss(mean_return, std_return)
        price = price * (1 + daily_return)
    ending_prices.append(price)

average_ending_price = sum(ending_prices) / len(ending_prices)

print(f"Simulated {simulations} runs for {days} days using real {ticker} data.")
print("Average ending price:", round(average_ending_price, 2))