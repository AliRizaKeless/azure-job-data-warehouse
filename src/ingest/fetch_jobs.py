import requests
import json
from datetime import datetime

URL = "https://arbeidsplassen.nav.no/public-feed/api/v1/ads?size=50"

def fetch_jobs():
    response = requests.get(URL)
    response.raise_for_status()
    return response.json()

def save_raw_data(data):
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    filename = f"data/raw/jobs_{timestamp}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Saved raw data to {filename}")

if __name__ == "__main__":
    data = fetch_jobs()
    save_raw_data(data)
