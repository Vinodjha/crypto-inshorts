from flask import Flask, render_template
from scraper import get_crypto_news

app = Flask(__name__)

@app.route("/")
def home():
    news = get_crypto_news()
    return render_template("index.html", news=news)

if __name__ == "__main__":
    app.run(debug=True)
# This is a simple Flask application that scrapes cryptocurrency news from CryptoPotato and displays it on a web page.
# The `get_crypto_news` function scrapes the news articles, and the `home` route renders the HTML template with the news data.
# The application runs in debug mode for development purposes.

