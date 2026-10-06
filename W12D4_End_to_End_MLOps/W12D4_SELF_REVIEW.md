\# W12D4 Self-Review



\## Checklist



\- \[x] ML API prepared

\- \[x] Docker containerization completed

\- \[x] Docker image build configured

\- \[x] GitHub Actions CI/CD workflow configured

\- \[x] Docker Hub publishing configured

\- \[x] Monitoring strategy documented

\- \[x] Retraining triggers documented

\- \[x] Execution evidence completed



\## Key Design Decision



Docker was used to provide a consistent runtime environment, while

GitHub Actions automates validation, Docker image building, and

publishing.



\## Hardest Part



The hardest part was connecting the different stages into one

repeatable workflow. This was handled by separating linting,

testing, containerization, and publishing into CI/CD steps.



\## Improvement



I would add automated integration tests, cloud deployment,

Prometheus/Grafana monitoring, and automated model retraining.

