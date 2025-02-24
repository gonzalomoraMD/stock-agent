import yfinance as yf
import ollama

def get_stock_price(symbol):
    stock = yf.Ticker(symbol)
    try:
        stock_price = stock.history(period="1d")["Close"].iloc[-1]  # Get latest close price
        return stock_price
    except Exception as e:
        return None  # Handle invalid symbols

def analyze_stock(symbol, price):
    prompt = f"Analyze the stock {symbol}. Its current price is {price:.2f}. Provide insights on its performance."
    response = ollama.chat(model="deepseek-r1:1.5b", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]

# Get user input
symbol = input("Enter stock symbol (e.g., AAPL for Apple): ").upper()
stock_price = get_stock_price(symbol)

if stock_price:
    analysis = analyze_stock(symbol, stock_price)
    print("\n🔹 AI Analysis:\n", analysis)
else:
    print("❌ Invalid stock symbol. Please try again.")
