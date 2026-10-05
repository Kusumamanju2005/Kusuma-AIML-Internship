import mlflow

# Use the same MLflow tracking database
mlflow.set_tracking_uri("sqlite:///mlflow.db")

# Replace this with the Best Run ID printed by mlflow_model_serving.py
best_run_id = "bbf28ee0f019421e84fc7ecf267bac66"

model_uri = f"runs:/{best_run_id}/model"

registered_model = mlflow.register_model(
    model_uri=model_uri,
    name="W11D3_RandomForest_Model"
)

print("\n========== MODEL REGISTRATION ==========")
print(f"Model Name: {registered_model.name}")
print(f"Model Version: {registered_model.version}")
print(f"Best Run ID: {best_run_id}")
print("Registration successful!")