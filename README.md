# Azure Job Data Warehouse

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
