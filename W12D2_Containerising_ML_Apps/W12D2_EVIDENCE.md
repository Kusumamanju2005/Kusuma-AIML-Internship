\# W12D2 Containerising ML Apps - Evidence



\## Objective



Containerize an ML prediction API using Docker and configure CI/CD

automation using GitHub Actions.



\## Docker Implementation



The ML API was packaged using Docker with Python 3.12.



Docker image:



kusuma-ml-api:latest



Build command:



docker build -t kusuma-ml-api:latest .



\## API



The Flask ML API provides:



\- GET /health

\- POST /predict



The prediction model uses the Iris dataset and RandomForestClassifier.



\## CI/CD



GitHub Actions was configured for:



1\. Code checkout

2\. Python environment setup

3\. Dependency installation

4\. Flake8 linting

5\. Python syntax testing

6\. Docker image building

7\. Docker Hub login

8\. Docker image publishing



\## Registry



Docker Hub repository:



kusu1803/kusuma-ml-api



\## Monitoring



The monitoring strategy tracks:



\- API response time

\- Request count

\- Error rate

\- Prediction latency

\- CPU and memory usage

\- Container health

\- Model prediction distribution

\- Data drift



\## Retraining Triggers



Retraining should be considered when:



\- Model accuracy decreases

\- New labelled data becomes available

\- Data drift is detected

\- Prediction quality decreases

\- Input data distribution changes significantly



\## Result



The ML API was successfully containerized and prepared for

automated CI/CD deployment.

