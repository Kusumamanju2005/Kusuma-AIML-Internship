\# W12D4 End-to-End MLOps Pipeline - Evidence



\## Objective



Build an end-to-end MLOps workflow covering development, testing,

containerization, CI/CD, deployment preparation, and monitoring.



\## Pipeline



The implemented workflow contains:



1\. ML API development

2\. Dependency management

3\. Code linting

4\. Python syntax testing

5\. Docker image creation

6\. Container deployment preparation

7\. GitHub Actions CI/CD

8\. Docker Hub image publishing

9\. Production monitoring strategy



\## ML API



The Flask API provides:



\- GET /health

\- POST /predict



The prediction service uses a RandomForestClassifier trained on

the Iris dataset.



\## Docker



Docker packages the application and its dependencies into a

portable container.



Image:



```text

kusuma-ml-api:latest

