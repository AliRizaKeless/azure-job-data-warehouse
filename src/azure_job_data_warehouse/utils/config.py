import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    raw_data_path: str
    processed_data_path: str
    warehouse_path: str
    azure_storage_account: str | None
    azure_storage_container: str | None


def get_config() -> Config:
    return Config(
        raw_data_path=os.getenv("RAW_DATA_PATH", "data/raw/jobs.json"),
        processed_data_path=os.getenv("PROCESSED_DATA_PATH", "data/processed/jobs_clean.csv"),
        warehouse_path=os.getenv("WAREHOUSE_PATH", "data/warehouse"),
        azure_storage_account=os.getenv("AZURE_STORAGE_ACCOUNT"),
        azure_storage_container=os.getenv("AZURE_STORAGE_CONTAINER"),
    )