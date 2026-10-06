\# W12D3 Self-Review



\## Checklist



\- \[x] Production ML API identified

\- \[x] API health monitoring documented

\- \[x] Infrastructure metrics documented

\- \[x] Data drift monitoring documented

\- \[x] Model performance monitoring documented

\- \[x] Alerts documented

\- \[x] Retraining triggers documented

\- \[x] CI/CD workflow documented

\- \[x] Execution evidence completed



\## Key Design Decision



Monitoring was designed to cover three areas: infrastructure health,

data quality, and model performance.



\## Hardest Part



The main challenge was identifying meaningful production signals

instead of monitoring only API availability. This was addressed by

including latency, errors, data drift, prediction distribution, and

model performance.



\## Improvement



With additional time, I would integrate Prometheus and Grafana,

automated drift detection, and automatic retraining pipelines.

