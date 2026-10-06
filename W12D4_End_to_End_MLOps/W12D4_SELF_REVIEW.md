\# W12D4 Self-Review



\## Checklist



\- \[x] ML API prepared

\- \[x] Dependencies documented

\- \[x] Docker containerization completed

\- \[x] CI/CD workflow configured

\- \[x] Docker image build configured

\- \[x] Docker Hub publishing configured

\- \[x] Production monitoring documented

\- \[x] Retraining triggers documented

\- \[x] End-to-end workflow documented



\## Key Design Decision



Docker was used to provide a consistent runtime environment, while

GitHub Actions automates validation and image publishing.



\## Hardest Part



The hardest part was connecting the different stages into one

repeatable workflow. This was handled by separating linting,

testing, containerization, and publishing into CI/CD steps.



\## Improvement



I would add automated integration tests, deployment to a cloud

platform, Prometheus/Grafana monitoring, and automated retraining.

