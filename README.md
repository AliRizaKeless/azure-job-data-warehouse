# Azure Job Data Warehouse
End-to-end Data Engineering Project using Python, SQL, and Azure

A small end-to-end data engineering project that ingests job market data, transforms it into structured datasets, models it as a star schema, and prepares it for SQL-based analytics on Azure.

## Project Goal

This project demonstrates a simple data warehouse pipeline using job market data and Azure cloud infrastructure.

## Architecture

Job API / Feed  
→ Raw JSON ingestion  
→ Transformation to structured CSV  
→ Star schema modeling  
→ SQL analytics layer  
→ Azure Blob Storage provisioned with Terraform  

## Tech Stack

- Python  
- SQL  
- Terraform  
- Azure Blob Storage  
- CSV / JSON  

## Project Structure

```text
src/
  ingest/
    fetch_jobs.py
  transform/
    transform_jobs.py
    build_star_schema.py

infra/
  main.tf

data/
  raw/
  processed/
  warehouse/

sql_queries.sql

Data Model

Fact Table
   fact_jobs
       job_id
       title
       company_id
       location_id
       date

Dimension Tables
   companies
       company_id
       company_name
   locations
       location_id
       location_name

Sample Output

Example Job Record
{
  "title": "Sjåfør og Montør",
  "company": "ARNESEN HVITEVARER AS",
  "location": "BERGEN",
  "date": "2023-06-14"
}

Example Aggregation
SELECT location, COUNT(*) as job_count
FROM fact_jobs
GROUP BY location
ORDER BY job_count DESC;

Example SQL Queries
Top companies by number of job postings
Jobs per location
Latest job postings

Infrastructure
Terraform provisions:
    Azure Resource Group
    Azure Storage Account
    Azure Storage Container

Future Improvements
    Add orchestration (e.g., Airflow)
    Load data into Azure SQL or Synapse
    Add data quality checks
    Automate pipeline with CI/CD

Status
Project in progress.
Current version includes ingestion, transformation, star schema modeling, SQL queries, and Azure infrastructure provisioning.
