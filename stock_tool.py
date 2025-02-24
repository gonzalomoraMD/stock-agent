import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def fetch_stock_data(ticker, period="6mo"):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    
    if data.empty:
        return "Invalid ticker or no data available."
    
    # Calculate moving averages
    data["50_MA"] = data["Close"].rolling(window=50).mean()
    data["200_MA"] = data["Close"].rolling(window=200).mean()
    
    # Plot the stock prices
    plt.figure(figsize=(10, 5))
    plt.plot(data["Close"], label="Closing Price", color="blue")
    plt.plot(data["50_MA"], label="50-day MA", color="red", linestyle="dashed")
    plt.plot(data["200_MA"], label="200-day MA", color="green", linestyle="dashed")
    
    plt.title(f"Stock Price of {ticker}")
    plt.legend()
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid()
    plt.savefig(f"{ticker}_stock_chart.png")  # Save the plot as an image
    plt.close()
    
    return f"Stock data for {ticker} fetched. Chart saved as {ticker}_stock_chart.png"

# Test function
if __name__ == "__main__":
    print(fetch_stock_data("AAPL"))
