import os
import requests

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")

def generate_summary(stock_data, news, ticker="STOCK"):
    name  = stock_data.get("name", ticker)
    price = stock_data.get("price", "N/A")
    open_ = stock_data.get("open", "N/A")
    high  = stock_data.get("high", "N/A")
    low   = stock_data.get("low", "N/A")
    news_titles = ", ".join([n["title"] for n in news[:3]])

    return f"""[0-10 sec | HOOK]
Did you check {name} today? Here is your 90 second brief!

[10-30 sec | SNAPSHOT]
{name} is trading at Rs {price}. Opened at Rs {open_}, high of Rs {high}, low of Rs {low}.

[30-60 sec | HAPPENING]
Recent news: {news_titles}. Strong volume shows active trader interest in this stock.

[60-80 sec | TAKEAWAY]
For beginners, focus on fundamentals not just daily price movement.

[80-90 sec | CTA]
Subscribe for daily stock briefs and always do your own research before investing!"""
