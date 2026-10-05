import mlflow


# Best run from W11D1 experiments
best_run_id = "089baea8c425470ab9b1c0373a840803"

# Model URI
model_uri = f"runs:/{best_run_id}/model"

# Register the best model
registered_model = mlflow.register_model(
    model_uri=model_uri,
    name="W11D1_RandomForest_Best_Model"
)

print("==========================================")
print("MODEL REGISTRATION SUCCESSFUL")
print("==========================================")

print(f"Model Name: {registered_model.name}")
print(f"Model Version: {registered_model.version}")
print(f"Run ID: {best_run_id}")