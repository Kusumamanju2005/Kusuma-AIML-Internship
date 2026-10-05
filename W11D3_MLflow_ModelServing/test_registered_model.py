import mlflow

# Use the same MLflow tracking database
mlflow.set_tracking_uri("sqlite:///mlflow.db")

# Change the version if your registration created a different version
model_name = "W11D3_RandomForest_Model"
model_version = "1"

model_uri = f"models:/{model_name}/{model_version}"

# Load registered model
model = mlflow.pyfunc.load_model(model_uri)

print("MODEL LOADED SUCCESSFULLY")
print(model)

# Test prediction
input_data = [[5.1, 3.5, 1.4, 0.2]]

prediction = model.predict(input_data)

print("\n========== PREDICTION TEST ==========")
print(f"Input: {input_data}")
print(f"Prediction: {prediction}")