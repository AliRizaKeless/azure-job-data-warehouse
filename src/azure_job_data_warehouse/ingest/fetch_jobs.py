import json
import logging
from datetime import UTC, datetime
from pathlib import Path

import requests

from src.azure_job_data_warehouse.utils.logging_config import configure_logging


configure_logging()
logger = logging.getLogger(__name__)

TOKEN_URL = "https://pam-stilling-feed.nav.no/api/publicToken"
FEED_URL = "https://pam-stilling-feed.nav.no/api/v1/feed"


def get_public_token() -> str:
    response = requests.get(TOKEN_URL, timeout=30)
    response.raise_for_status()

    raw_text = response.text.strip()

    return raw_text.split()[-1]


def fetch_jobs() -> dict:
    logger.info("Fetching jobs from API")

    token = get_public_token()

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {token}",
    }

    response = requests.get(FEED_URL, headers=headers, timeout=30)
    response.raise_for_status()

    logger.info("Successfully fetched job data")

    return response.json()


def save_raw_data(data: dict) -> None:
    timestamp = datetime.now(UTC).strftime("%Y%m%d_%H%M%S")

    output_dir = Path("data/raw")
    output_dir.mkdir(parents=True, exist_ok=True)

    filename = output_dir / f"jobs_{timestamp}.json"

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    logger.info("Saved raw data to %s", filename)


if __name__ == "__main__":
    job_data = fetch_jobs()
    save_raw_data(job_data)