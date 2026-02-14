import yfinance as yf

def get_stock_price(code):
    ticker = yf.Ticker(code)
    data = ticker.history(period="1d")

    if data.empty:
        return None

    return float(data["Close"].iloc[0])
