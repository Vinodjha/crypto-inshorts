import requests
from datetime import datetime

def get_crypto_news():
    url = "https://min-api.cryptocompare.com/data/v2/news/?lang=EN"
    response = requests.get(url)
    data = response.json()

    articles = []

    for item in data["Data"]:
        title = item["title"]
        link = item["url"]
        source = item.get("source", "CryptoCompare")
        
        # Use the 'body' as a quick summary and limit to 200 characters
        raw_summary = item.get("body", "")
        summary = raw_summary[:200] + "..." if len(raw_summary) > 200 else raw_summary

        articles.append({
            "title": title,
            "link": link,
            "source": source,
            "summary": summary
        })

    print(f"Total articles found: {len(articles)}")
    return articles
