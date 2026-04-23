import yfinance as yf
import requests

TICKERS = ["AAPL","MSFT","NVDA","TSLA","AMZN"]

TOKEN = os.getenv(8274803396:aafa-exhmbewsvkal0x4x2tn1syul2uxkaa)
CHAT_ID = os.getenv(8797190988)

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
    
