import csv
import json
import logging
from pathlib import Path

from src.azure_job_data_warehouse.utils.logging_config import configure_logging


configure_logging()
logger = logging.getLogger(__name__)

RAW_DATA_DIR = Path("data/raw")
OUTPUT_FILE = Path("data/processed/jobs.csv")


def get_latest_raw_file() -> Path:
    json_files = sorted(RAW_DATA_DIR.glob("jobs_*.json"))

    if not json_files:
        raise FileNotFoundError("No raw job files found")

    return json_files[-1]


def transform() -> None:
    input_file = get_latest_raw_file()

    logger.info("Reading raw data from %s", input_file)

    with open(input_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    jobs = data["items"]

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow([
            "job_id",
            "title",
            "company",
            "location",
            "date",
        ])

        for job in jobs:
            entry = job["_feed_entry"]

            job_id = entry.get("uuid")
            title = entry.get("title")
            company = entry.get("businessName")
            location = entry.get("municipal")
            date = entry.get("sistEndret")

            writer.writerow([
                job_id,
                title,
                company,
                location,
                date,
            ])

    logger.info("Saved transformed data to %s", OUTPUT_FILE)


if __name__ == "__main__":
    transform()