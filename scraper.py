import requests
import asyncio
from crawl4ai import AsyncWebCrawler
from summarizer import summarize_text


from bs4 import BeautifulSoup
import re

import re

def clean_markdown(md: str) -> str:
    cleaned_lines = []
    for line in md.splitlines():
        line = line.strip()

        # Skip empty or ultra short lines
        if not line or len(line) < 25:
            continue

        # Skip image lines or linked images
        if line.startswith("![") or "[![" in line:
            continue

        # Skip social/media/link clusters
        if any(domain in line.lower() for domain in [
            "facebook", "twitter", "telegram", "instagram",
            "linkedin", "reddit", "youtube", "whatsapp",
            "coinmarketcap", "coingecko", "subscribe", "comment", "newsletter"
        ]):
            continue

        # Skip link-only lines
        if re.fullmatch(r"\[.*?\]\(.*?\)", line):
            continue

        # Skip lines with mostly emojis or symbols
        if re.match(r"^[\W\d\s]{10,}$", line):
            continue

        # Skip lines with only repeated words
        if re.match(r"^(.*?)\1+$", line.replace(" ", "")):
            continue

        cleaned_lines.append(line)

    return "\n\n".join(cleaned_lines)


async def fetch_full_article(url):
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url)
        html = result.html

        # Parse HTML using BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")

        # Heuristic: find main content via <article> or <div> with class-like 'content'
        article = soup.find("article")
        if not article:
            article = soup.find("div", class_=re.compile(r"(content|main|article|body)", re.I))

        if not article:
            return "Could not find main content."

        # Extract all paragraph and heading text
        content_lines = []
        for tag in article.find_all(["p", "h1", "h2", "h3", "blockquote"]):
            text = tag.get_text(strip=True)
            if len(text) > 30:
                content_lines.append(text)

        return "\n\n".join(content_lines)




# Main fetcher: gets news and summaries
def get_crypto_news():
    url = "https://min-api.cryptocompare.com/data/v2/news/?lang=EN"
    response = requests.get(url)
    data = response.json()
    
    articles = [
        {
            "title": item["title"],
            "link": item["url"],
            "source": item.get("source", "CryptoCompare")
        }
        for item in data["Data"][:10]  # Limit to 3 for faster testing
    ]

    # Fetch summaries using event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    full_articles = loop.run_until_complete(
    asyncio.gather(*(fetch_full_article(a["link"]) for a in articles))
)

# Attach full article text to each
    for article, full_text in zip(articles, full_articles):
        article["full_text"] = full_text

    return articles



if __name__ == "__main__":
    articles = get_crypto_news()
    for i, article in enumerate(articles):
        if not article.get("full_text") or not article["full_text"].strip():
            print("Skipping empty article:", article["title"])
            continue
        print(f"\n--- Article {i+1} ---")
        print("Title:", article["title"])
        print("Link:", article["link"])
        print("Source:", article["source"])
        print("\nFull Article (start):")
        print(article["full_text"][:200])  # Print first 500 characters only

        print("...\n")
        print("--- Summary ---")
        print(summarize_text(article["full_text"]))
        print("...\n \n")
