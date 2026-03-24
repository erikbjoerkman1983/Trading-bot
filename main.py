import yfinance as yf
import requests

TICKERS = ["AAPL","MSFT","NVDA","TSLA","AMZN"]

TOKEN = "DIN_TELEGRAM_TOKEN"
CHAT_ID = "DIN_CHAT_ID"

def send_alert(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def analyze(ticker):
    data = yf.download(ticker, period="3mo")

    ma50 = data["Close"].rolling(50).mean().iloc[-1]
    price = data["Close"].iloc[-1]

    return f"{ticker}: {'BULL' if price > ma50 else 'BEAR'}"

def run():
    results = [analyze(t) for t in TICKERS]
    send_alert("\n".join(results))

if __name__ == "__main__":
    run()
    