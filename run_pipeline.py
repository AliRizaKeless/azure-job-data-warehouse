import subprocess

def run_step(command, step_name):
    print(f"Running: {step_name}")
    result = subprocess.run(command, shell=True)

    if result.returncode != 0:
        print(f"Error in step: {step_name}")
        exit(1)

def main():
    run_step("python src/ingest/fetch_jobs.py", "Ingestion")
    run_step("python src/transform/transform_jobs.py", "Transformation")
    run_step("python src/transform/build_star_schema.py", "Star Schema")

    print("Pipeline completed successfully!")

if __name__ == "__main__":
    main()