import requests
import os
from dotenv import load_dotenv

# Load token from ini.env (you named it differently, so pass filename)
load_dotenv("ini.env")
HUGGINGFACE_API_TOKEN = os.getenv("HF_API_TOKEN")
print("Token loaded?", bool(HUGGINGFACE_API_TOKEN))

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}

def summarize_text(text: str) -> str:
    payload = {"inputs": text[:1024]}  # limit to 1024 chars for safety

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        summary = response.json()[0]["summary_text"]
        return summary.strip()
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        print("Response text:", response.text)
        return "Summary not available."

