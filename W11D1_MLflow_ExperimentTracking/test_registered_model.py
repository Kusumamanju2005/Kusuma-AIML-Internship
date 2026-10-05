import mlflow


model = mlflow.pyfunc.load_model(
    "models:/W11D1_RandomForest_Best_Model/1"
)

sample_data = [
    [5.1, 3.5, 1.4, 0.2]
]

prediction = model.predict(sample_data)

print("==========================================")
print("REGISTERED MODEL TEST")
print("==========================================")

print("Input:", sample_data)
print("Prediction:", prediction)
print("Model loaded and prediction completed successfully.")