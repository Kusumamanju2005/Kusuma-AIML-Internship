\# W11D3 Self Review



\## Task Checklist



\- \[x] Created MLflow experiment for model serving

\- \[x] Logged model parameters

\- \[x] Logged accuracy metrics

\- \[x] Logged model artifact

\- \[x] Ran 5 experiments with different hyperparameters

\- \[x] Identified the best model

\- \[x] Registered the best model in MLflow Model Registry

\- \[x] Loaded the registered model successfully

\- \[x] Tested prediction successfully

\- \[x] Started MLflow model server

\- \[x] Verified REST API port 5001

\- \[x] Tested REST API prediction endpoint with POST request

\- \[x] Added final REST API response evidence



\## Best Result



\- Best Accuracy: 0.9667

\- Best Run ID: bbf28ee0f019421e84fc7ecf267bac66

\- Registered Model: W11D3\_RandomForest\_Model

\- Model Version: 1



\## Prediction Test



Input:



\[\[5.1, 3.5, 1.4, 0.2]]



Prediction:



\[0]



\## Model Serving



MLflow model server successfully started on port 5001.

\## REST API Test



\- Endpoint: http://127.0.0.1:5001/invocations

\- Method: POST

\- Status Code: 200

\- Response: {"predictions": \[0]}

\- Result: REST API prediction successful.



REST endpoint:



http://127.0.0.1:5001/invocations



Port verification:



TcpTestSucceeded: True



\## Learning



I learned how to track experiments using MLflow, register the best model, load the registered model, and expose it through an MLflow REST API server.



\## Final Status



Implementation is mostly complete. REST API prediction testing remains to be verified.

