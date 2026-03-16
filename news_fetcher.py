import requests
import xml.etree.ElementTree as ET
from datetime import datetime

def get_news(company, max_articles=5):
    try:
        rss_url = "https://economictimes.indiatimes.com/rssfeedstopstories.cms"
        resp = requests.get(rss_url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        root = ET.fromstring(resp.text)
        items = root.findall(".//item")
        articles = []
        for item in items:
            title = item.findtext("title") or ""
            articles.append({
                "title": title,
                "source": "Economic Times",
                "url": item.findtext("link") or "",
                "published": item.findtext("pubDate") or ""
            })
            if len(articles) >= max_articles:
                break
        return articles if articles else [{"title": f"{company} stock in focus today", "source": "FinVise", "url": "", "published": ""}]
    except Exception as e:
        return [{"title": f"{company} stock in focus today", "source": "FinVise", "url": "", "published": ""}]
