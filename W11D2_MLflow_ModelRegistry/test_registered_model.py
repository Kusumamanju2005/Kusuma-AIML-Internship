import mlflow


# Use W11D2 tracking database
mlflow.set_tracking_uri("sqlite:///mlflow.db")


# Load registered model version 2
model = mlflow.pyfunc.load_model(
    "models:/W11D2_RandomForest_Model/2"
)


# Iris sample
sample_data = [
    [5.1, 3.5, 1.4, 0.2]
]


# Generate prediction
prediction = model.predict(sample_data)


print("==========================================")
print("REGISTERED MODEL TEST")
print("==========================================")

print("Input:", sample_data)
print("Prediction:", prediction)
print("Model loaded and prediction completed successfully.")