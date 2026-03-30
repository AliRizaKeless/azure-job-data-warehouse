-- Top companies by number of job postings
SELECT company_id, COUNT(*) as job_count
FROM fact_jobs
GROUP BY company_id
ORDER BY job_count DESC;

-- Jobs per location
SELECT location_id, COUNT(*) as job_count
FROM fact_jobs
GROUP BY location_id
ORDER BY job_count DESC;

-- Latest job postings
SELECT *
FROM fact_jobs
ORDER BY date DESC
LIMIT 10;