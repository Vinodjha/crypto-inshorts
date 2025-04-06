# app.py
# --------------------------
# Flask app to serve summarized crypto news
# --------------------------

from flask import Flask, render_template
from scraper import get_crypto_news
from summarizer import summarize_text

app = Flask(__name__)

@app.route("/")
def index():
    # Fetch crypto news articles with full text
    articles = get_crypto_news()

    # Add summaries (skip if full_text is missing or too short)
    summarized = []
    for article in articles:
        full_text = article.get("full_text", "").strip()

        if not full_text or len(full_text) < 100:
            continue

        try:
            article["summary"] = summarize_text(full_text)
        except Exception as e:
            print("Error during summarization:", e)
            article["summary"] = "Summary not available."

        summarized.append(article)

    return render_template("index.html", news=summarized)

if __name__ == "__main__":
    app.run(debug=True)

# app.py
# This is a simple Flask application that scrapes cryptocurrency news from CryptoPotato and displays it on a web page.
# The `get_crypto_news` function scrapes the news articles, and the `home` route renders the HTML template with the news data.
# The application runs in debug mode for development purposes.

