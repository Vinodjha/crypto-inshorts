
# 🧠 Crypto News Summarization Project

## 🚀 Project Overview

This project is a real-time crypto news aggregator and summarizer. It scrapes articles from reliable sources using NLP-powered tools, cleans the raw HTML content, and summarizes it using transformer models from Hugging Face.

---

## 📦 Requirements

- Python >= 3.8
- Flask
- requests, asyncio, re
- beautifulsoup4
- crawl4ai
- transformers
- python-dotenv

Install requirements using:

```bash
pip install -r requirements.txt
```

---

## 📁 Structure

```
crypto-news/
│
├── app.py               # Flask backend
├── scraper.py           # Async web scraper and cleaner
├── summarizer.py        # Summarizer using Hugging Face API
├── templates/
│   └── index.html       # Simple UI
├── ini.env              # Hugging Face token storage
├── requirements.txt     # Package list
```

---

## 🔄 Workflow

1. `scraper.py` fetches top headlines using CryptoCompare API.
2. Extracts full article using **Crawl4AI**.
3. Cleans the HTML with **BeautifulSoup** and regex filters.
4. `summarizer.py` sends clean content to Hugging Face summarizer.
5. `app.py` serves summaries through a Flask web interface.

---

## 🛠️ Technologies Used

### Crawl4AI (Web Scraper)
An open-source NLP-based web scraper that detects relevant content on pages automatically — no custom parser needed.

### BeautifulSoup (Cleaner)
Extracts readable sections from parsed HTML. Removes navbars, links, ads, and other noisy content.

### Hugging Face Transformers API
The hosted model (`facebook/bart-large-cnn`) is used to summarize articles remotely, avoiding local heavy computation.

---

## 🧹 Cleaning Pipeline

We filtered lines:
- < 25 characters
- Image links, repetitive phrases
- Pure emoji/symbol content
- Junk from social media or comments

Example:

```
Original: [Facebook] [Telegram] Subscribe now!
Cleaned : Ethereum drops 46%, but analysts remain hopeful for $5K recovery in 2025.
```

---

## ✅ Skills Demonstrated

- API Integration
- NLP Web Scraping
- HTML Parsing
- Regex Filtering
- Transformer Summarization
- Async Python
- Flask Backend
- Minimal UI Design

---

## 📣 LinkedIn Summary (Ready-to-Post)

🚀 Just wrapped up a real-time **Crypto News Summarizer** project!

🔍 What it does:
- Fetches trending crypto headlines
- Extracts article with **Crawl4AI**
- Cleans junk HTML with **BeautifulSoup**
- Summarizes via **Hugging Face Transformers API**
- Displays it using **Flask UI**

🛠️ Python | Flask | NLP | Regex | APIs | Transformers | AsyncIO
