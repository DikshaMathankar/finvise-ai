import yfinance as yf

def get_stock_data(ticker, exchange="NSE"):
    suffix = ".NS" if exchange == "NSE" else ".BO"
    symbol = ticker.upper() + suffix
    try:
        stock = yf.Ticker(symbol)
        info = stock.info
        price = info.get("currentPrice") or info.get("regularMarketPrice")
        return {
            "name": info.get("longName") or ticker,
            "price": round(float(price), 2) if price else "N/A",
            "open": round(float(info.get("open") or 0), 2),
            "high": round(float(info.get("dayHigh") or 0), 2),
            "low": round(float(info.get("dayLow") or 0), 2),
            "volume": int(info.get("volume") or 0),
            "prev_close": round(float(info.get("previousClose") or 0), 2),
            "pe_ratio": info.get("trailingPE", "N/A"),
        }
    except Exception as e:
        return {
            "name": ticker,
            "price": "N/A",
            "open": "N/A",
            "high": "N/A",
            "low": "N/A",
            "volume": 0,
            "prev_close": "N/A",
            "pe_ratio": "N/A"
        }
