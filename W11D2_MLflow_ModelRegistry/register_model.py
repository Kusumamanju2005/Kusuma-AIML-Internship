import mlflow


# Use the same tracking database as W11D2 experiments
mlflow.set_tracking_uri("sqlite:///mlflow.db")


# Best run from W11D2
best_run_id = "1baa7eeaeb534fd5bc0377f4f9cc1e7a"

# Model URI
model_uri = f"runs:/{best_run_id}/model"


# Register best model
registered_model = mlflow.register_model(
    model_uri=model_uri,
    name="W11D2_RandomForest_Model"
)


print("==========================================")
print("MODEL REGISTRATION SUCCESSFUL")
print("==========================================")

print(f"Model Name: {registered_model.name}")
print(f"Model Version: {registered_model.version}")
print(f"Best Run ID: {best_run_id}")