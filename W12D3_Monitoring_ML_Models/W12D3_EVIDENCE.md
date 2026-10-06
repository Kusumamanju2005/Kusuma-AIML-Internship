\# W12D3 Monitoring ML Models - Evidence



\## Objective



Create a production monitoring strategy for a containerized ML API.



\## ML API



The Flask ML API exposes:



\- GET /health

\- POST /predict



The API uses a RandomForestClassifier trained on the Iris dataset.



\## Production Metrics



The following metrics should be monitored:



\- API response time

\- Request count

\- HTTP error rate

\- Prediction latency

\- CPU usage

\- Memory usage

\- Container health

\- Model prediction distribution



\## Data Monitoring



Data drift should be monitored by comparing production input

distributions with the training data distribution.



Important checks include:



\- Feature distribution changes

\- Missing values

\- Unexpected input ranges

\- Changes in prediction distribution



\## Model Monitoring



Model quality should be monitored using:



\- Accuracy

\- Precision

\- Recall

\- F1-score

\- Prediction distribution



when labelled production data becomes available.



\## Alerts



Alerts should be configured when:



\- Error rate exceeds 5%

\- Response time remains above 1 second

\- Container becomes unhealthy

\- CPU or memory remains high

\- Significant data drift is detected

\- Model performance falls below the required threshold



\## Retraining Triggers



Retraining should be considered when:



\- Model accuracy decreases

\- Significant data drift is detected

\- New labelled data becomes available

\- Prediction quality degrades

\- Production data differs significantly from training data



\## CI/CD



The existing GitHub Actions workflow performs:



1\. Lint

2\. Test

3\. Docker image build

4\. Docker Hub publishing



\## Conclusion



The monitoring strategy provides visibility into API health,

data quality, model performance, and infrastructure usage.

