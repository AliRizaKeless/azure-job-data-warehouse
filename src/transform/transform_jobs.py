import json
import csv
from pathlib import Path

INPUT_FILE = "data/raw/jobs_20260330_194543.json"
OUTPUT_FILE = "data/processed/jobs.csv"

def transform():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    jobs = data["items"]

    output_dir = Path("data/processed")
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        # header
        writer.writerow(["job_id", "title", "company", "location", "date"])

        for job in jobs:
            entry = job["_feed_entry"]

            job_id = entry.get("uuid")
            title = entry.get("title")
            company = entry.get("businessName")
            location = entry.get("municipal")
            date = entry.get("sistEndret")

            writer.writerow([job_id, title, company, location, date])

    print(f"Saved transformed data to {OUTPUT_FILE}")

if __name__ == "__main__":
    transform()