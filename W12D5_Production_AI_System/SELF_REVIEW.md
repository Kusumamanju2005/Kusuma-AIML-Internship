\# W12D5 Self-Review



\## Checklist



\- \[x] ML API implemented

\- \[x] Docker container created

\- \[x] Docker image built

\- \[x] API health endpoint available

\- \[x] Prediction endpoint available

\- \[x] CI/CD workflow configured

\- \[x] Docker Hub publishing configured

\- \[x] Monitoring strategy documented

\- \[x] Retraining triggers documented

\- \[x] Execution evidence documented



\## Key Design Decision



The ML API was packaged as a Docker container so that the application

and its dependencies can run consistently across environments.

GitHub Actions was used to automate validation and image publishing.



\## Hardest Part



The main challenge was combining the application, Docker, CI/CD,

and monitoring requirements into one production-oriented workflow.



\## Improvement



I would add automated integration tests, cloud deployment,

Prometheus/Grafana dashboards, centralized logging, model drift

detection, and automated retraining.

