import csv
from pathlib import Path

INPUT_FILE = "data/processed/jobs.csv"

def build_star_schema():
    companies = {}
    locations = {}

    fact_rows = []

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            company_name = row["company"]
            location_name = row["location"]

            # company dimension
            if company_name not in companies:
                companies[company_name] = len(companies) + 1

            # location dimension
            if location_name not in locations:
                locations[location_name] = len(locations) + 1

            fact_rows.append({
                "job_id": row["job_id"],
                "title": row["title"],
                "company_id": companies[company_name],
                "location_id": locations[location_name],
                "date": row["date"]
            })

    # output klasörü
    output_dir = Path("data/warehouse")
    output_dir.mkdir(parents=True, exist_ok=True)

    # companies table
    with open(output_dir / "companies.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["company_id", "company_name"])
        for name, cid in companies.items():
            writer.writerow([cid, name])

    # locations table
    with open(output_dir / "locations.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["location_id", "location_name"])
        for name, lid in locations.items():
            writer.writerow([lid, name])

    # fact table
    with open(output_dir / "fact_jobs.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["job_id", "title", "company_id", "location_id", "date"])
        for row in fact_rows:
            writer.writerow(row.values())

    print("Star schema created!")

if __name__ == "__main__":
    build_star_schema()