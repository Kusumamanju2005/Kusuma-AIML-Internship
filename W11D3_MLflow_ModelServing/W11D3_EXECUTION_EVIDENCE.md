\# W11D3 Execution Evidence



\## 1. MLflow Experiment Tracking



\- Experiment: `W11D3\_MLflow\_Model\_Serving`

\- Dataset: Iris Dataset

\- Model: RandomForestClassifier

\- Number of experiments: 5

\- Parameters logged: `n\_estimators`, `max\_depth`

\- Metric logged: Accuracy

\- Model artifact logged: Yes



\## 2. Best Model



\- Best Accuracy: `0.9667`

\- Best Run ID: `bbf28ee0f019421e84fc7ecf267bac66`



\## 3. Model Registry



\- Registered Model: `W11D3\_RandomForest\_Model`

\- Model Version: `1`

\- Registration: Successful



\## 4. Model Loading



The registered model was successfully loaded from MLflow Model Registry.



\## 5. Prediction Test



Input:



```text

\[\[5.1, 3.5, 1.4, 0.2]]

Prediction:



\[0]



\## 6. MLflow Model Serving



MLflow model serving was successfully started using Uvicorn.



Server:



```text

http://0.0.0.0:5001

