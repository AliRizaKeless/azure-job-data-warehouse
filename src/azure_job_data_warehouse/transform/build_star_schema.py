import csv
import logging
from pathlib import Path

from src.azure_job_data_warehouse.utils.logging_config import configure_logging


configure_logging()
logger = logging.getLogger(__name__)

INPUT_FILE = Path("data/processed/jobs.csv")
OUTPUT_DIR = Path("data/warehouse")


def build_star_schema() -> None:
    logger.info("Building star schema")

    companies: dict[str, int] = {}
    locations: dict[str, int] = {}

    fact_rows: list[dict] = []

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            company_name = row["company"]
            location_name = row["location"]

            if company_name not in companies:
                companies[company_name] = len(companies) + 1

            if location_name not in locations:
                locations[location_name] = len(locations) + 1

            fact_rows.append({
                "job_id": row["job_id"],
                "title": row["title"],
                "company_id": companies[company_name],
                "location_id": locations[location_name],
                "date": row["date"],
            })

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    write_companies_table(companies)
    write_locations_table(locations)
    write_fact_table(fact_rows)

    logger.info("Star schema created successfully")


def write_companies_table(companies: dict[str, int]) -> None:
    with open(
        OUTPUT_DIR / "companies.csv",
        "w",
        newline="",
        encoding="utf-8",
    ) as file:
        writer = csv.writer(file)

        writer.writerow([
            "company_id",
            "company_name",
        ])

        for name, company_id in companies.items():
            writer.writerow([company_id, name])


def write_locations_table(locations: dict[str, int]) -> None:
    with open(
        OUTPUT_DIR / "locations.csv",
        "w",
        newline="",
        encoding="utf-8",
    ) as file:
        writer = csv.writer(file)

        writer.writerow([
            "location_id",
            "location_name",
        ])

        for name, location_id in locations.items():
            writer.writerow([location_id, name])


def write_fact_table(fact_rows: list[dict]) -> None:
    with open(
        OUTPUT_DIR / "fact_jobs.csv",
        "w",
        newline="",
        encoding="utf-8",
    ) as file:
        writer = csv.writer(file)

        writer.writerow([
            "job_id",
            "title",
            "company_id",
            "location_id",
            "date",
        ])

        for row in fact_rows:
            writer.writerow(row.values())


if __name__ == "__main__":
    build_star_schema()