\# W12D2 Self-Review



\## Checklist



\- \[x] ML API containerized with Docker

\- \[x] Docker image built successfully

\- \[x] Docker API configured on port 5000

\- \[x] GitHub Actions CI/CD workflow configured

\- \[x] Docker Hub publishing configured

\- \[x] Monitoring strategy documented

\- \[x] Retraining triggers documented

\- \[x] Execution evidence completed



\## Key Design Decision



A lightweight Python Docker image was used to package the Flask ML API.

GitHub Actions automates linting, testing, Docker image building, and

publishing.



\## Hardest Part



The main challenge was configuring Docker and connecting the CI/CD

workflow with Docker Hub. This was solved by testing the Docker image

locally and configuring Docker Hub credentials as GitHub secrets.



\## Improvement



I would add automated API endpoint tests, health checks, Prometheus

metrics, Grafana dashboards, and automated model drift detection.

