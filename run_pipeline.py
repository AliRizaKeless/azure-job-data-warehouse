import logging
import subprocess
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def run_step(command, step_name):
    logging.info("Starting step: %s", step_name)
    result = subprocess.run(command, shell=True)

    if result.returncode != 0:
        logging.error("Step failed: %s", step_name)
        sys.exit(1)

    logging.info("Completed step: %s", step_name)

def main():
    run_step("python src/ingest/fetch_jobs.py", "Ingestion")
    run_step("python src/transform/transform_jobs.py", "Transformation")
    run_step("python src/transform/build_star_schema.py", "Star Schema")
    logging.info("Pipeline completed successfully!")

if __name__ == "__main__":
    main()