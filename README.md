
#  Crypto News Summarization Project

## Project Overview

This project is a real-time crypto news aggregator and summarizer. It scrapes articles from reliable sources using NLP-powered tools, cleans the raw HTML content, and summarizes it using transformer models from Hugging Face.

---

##  Requirements

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

##  Structure

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

## Workflow

1. `scraper.py` fetches top headlines using CryptoCompare API.
2. Extracts full article using **Crawl4AI**.
3. Cleans the HTML with **BeautifulSoup** and regex filters.
4. `summarizer.py` sends clean content to Hugging Face summarizer.
5. `app.py` serves summaries through a Flask web interface.

---

## Technologies Used

### Crawl4AI (Web Scraper)
Crawl4AI is an open-source NLP-based scraper that automatically understands and extracts the main content from webpages — without knowing the site's structure in advance. Unlike traditional scrapers, it uses NLP signals to detect the most relevant section of an article.

- Used here to fetch HTML from crypto news links

- Handles dynamic layouts and article-heavy pages well

- Easily integrates with asyncio for concurrent scraping

### BeautifulSoup (Cleaner)
BeautifulSoup is a Python library that parses and navigates HTML/XML content. In this project:

- It's used to locate content within <article>, <div>, and <p> tags

- Filters out layout junk like navbars, social links, ads

- Helps format the cleaned paragraphs for summarization

### Hugging Face Transformers API
The hosted model (`facebook/bart-large-cnn`) is used to summarize articles remotely, avoiding local heavy computation.

**facebook/bart-large-cnn**
- Type: Transformer-based Sequence-to-Sequence model
- Architecture: BART (Bidirectional and Auto-Regressive Transformers)
- Trained by: Facebook AI
- Use-case: Summarization of long documents or news articles

 How It Works
BART is a denoising autoencoder for pretraining sequence-to-sequence models. It combines the best of:

BERT: Bidirectional encoder (good at understanding context)

GPT: Left-to-right decoder (good at text generation)

facebook/bart-large-cnn is a fine-tuned version of BART specifically for summarizing long texts (like news articles). It was trained on the CNN/DailyMail dataset, which contains thousands of news articles paired with human-written summaries.

---

## Cleaning Pipeline

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

## Skills Involved

- API Integration
- NLP Web Scraping
- HTML Parsing
- Regex Filtering
- Transformer Summarization
- Async Python
- Flask Backend
- Minimal UI Design



 Python | Flask | NLP | Regex | APIs | Transformers | AsyncIO
