import requests
import json
from datetime import datetime
from pathlib import Path

TOKEN_URL = "https://pam-stilling-feed.nav.no/api/publicToken"
FEED_URL = "https://pam-stilling-feed.nav.no/api/v1/feed"

def get_public_token():
    response = requests.get(TOKEN_URL, timeout=30)
    response.raise_for_status()
    raw_text = response.text.strip()
    return raw_text.split()[-1]

def fetch_jobs():
    token = get_public_token()
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {token}",
    }

    response = requests.get(FEED_URL, headers=headers, timeout=30)
    response.raise_for_status()
    return response.json()

def save_raw_data(data):
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    output_dir = Path("data/raw")
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = output_dir / f"jobs_{timestamp}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Saved raw data to {filename}")

if __name__ == "__main__":
    data = fetch_jobs()
    save_raw_data(data)