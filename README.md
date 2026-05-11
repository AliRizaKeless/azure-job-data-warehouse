# Azure Job Data Warehouse

End-to-end data engineering project that ingests job market data, transforms raw JSON into structured datasets, models the data using a star schema, and prepares it for SQL-based analytics on Azure.

---

## Project Goal

The goal of this project is to demonstrate a cloud-oriented data warehouse pipeline using Python, SQL, and Azure infrastructure.

This project covers the core stages of a modern data engineering workflow:

- Raw data ingestion
- Data transformation
- Star schema modeling
- SQL analytics
- Azure Blob Storage provisioning with Terraform

---

## Architecture

- Job API / Feed
  ↓
- Raw JSON Data
  ↓
- Python Transformation Layer
  ↓
- Processed CSV Datasets
  ↓
- Star Schema Warehouse Tables
  ↓
- SQL Analytics Layer
  ↓
- Azure Blob Storage

---

## Tech Stack

- Python
- SQL
- Terraform
- Azure Blob Storage
- CSV / JSON
- Git & GitHub

---

## Project Structure

```text
azure-job-data-warehouse/
├── data/
│   ├── raw/
│   ├── processed/
│   └── warehouse/
│
├── infra/
│   └── main.tf
│
├── src/
│   └── azure_job_data_warehouse/
│       ├── ingest/
│       │   └── fetch_jobs.py
│       ├── transform/
│       │   ├── transform_jobs.py
│       │   └── build_star_schema.py
│       └── utils/
│
├── tests/
├── run_pipeline.py
├── sql_queries.sql
├── requirements.txt
└── README.md
```

---
Data Model
The warehouse layer follows a basic star schema design.

Fact Table
fact_jobs

| Column      | Description                        |
| ----------- | ---------------------------------- |
| job_id      | Unique job identifier              |
| title       | Job title                          |
| company_id  | Foreign key to companies dimension |
| location_id | Foreign key to locations dimension |
| date        | Job posting date                   |

Dimension Tables
companies

| Column       | Description               |
| ------------ | ------------------------- |
| company_id   | Unique company identifier |
| company_name | Company name              |

locations

| Column        | Description                |
| ------------- | -------------------------- |
| location_id   | Unique location identifier |
| location_name | Location name              |

Example Record
{
  "title": "Sjåfør og Montør",
  "company": "ARNESEN HVITEVARER AS",
  "location": "BERGEN",
  "date": "2023-06-14"
}

Example SQL Query
SELECT location, COUNT(*) AS job_count
FROM fact_jobs
GROUP BY location
ORDER BY job_count DESC;

How to Run
Install dependencies:
pip install -r requirements.txt
Run the pipeline:
python run_pipeline.py

Infrastructure
Terraform provisions the following Azure resources:
Azure Resource Group
Azure Storage Account
Azure Storage Container

Current Status
The current version includes:
Raw data ingestion
JSON-to-CSV transformation
Star schema generation
SQL analytics queries
Azure Blob Storage infrastructure provisioning

Roadmap
Planned improvements:
Add Docker support
Add structured logging
Add automated tests
Add data quality checks
Add orchestration with Apache Airflow
Load curated warehouse tables into Azure SQL or Synapse
Add CI/CD with GitHub Actions

Author
Ali Rıza Keles
