import logging
import subprocess
import sys

from src.azure_job_data_warehouse.utils.logging_config import configure_logging


configure_logging()
logger = logging.getLogger(__name__)


def run_step(command: str, step_name: str) -> None:
    logger.info("Starting step: %s", step_name)

    result = subprocess.run(command, shell=True)

    if result.returncode != 0:
        logger.error("Step failed: %s", step_name)
        sys.exit(1)

    logger.info("Completed step: %s", step_name)


def main() -> None:
    run_step(
        "python src/azure_job_data_warehouse/ingest/fetch_jobs.py",
        "Ingestion",
    )
    run_step(
        "python src/azure_job_data_warehouse/transform/transform_jobs.py",
        "Transformation",
    )
    run_step(
        "python src/azure_job_data_warehouse/transform/build_star_schema.py",
        "Star Schema",
    )

    logger.info("Pipeline completed successfully!")


if __name__ == "__main__":
    main()