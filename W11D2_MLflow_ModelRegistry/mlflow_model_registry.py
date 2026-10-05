import mlflow
import mlflow.sklearn

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# ==========================================
# LOAD DATA
# ==========================================

X, y = load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# ==========================================
# MLFLOW SETUP
# ==========================================

mlflow.set_experiment(
    "W11D2_Model_Registry_Experiments"
)


# ==========================================
# HYPERPARAMETER EXPERIMENTS
# ==========================================

experiments = [
    {"n_estimators": 50, "max_depth": 3},
    {"n_estimators": 50, "max_depth": 5},
    {"n_estimators": 100, "max_depth": 3},
    {"n_estimators": 100, "max_depth": 5},
    {"n_estimators": 150, "max_depth": 7},
]


best_accuracy = 0.0
best_run_id = None


# ==========================================
# RUN EXPERIMENTS
# ==========================================

for params in experiments:

    with mlflow.start_run() as run:

        model = RandomForestClassifier(
            n_estimators=params["n_estimators"],
            max_depth=params["max_depth"],
            random_state=42
        )

        model.fit(
            X_train,
            y_train
        )

        predictions = model.predict(
            X_test
        )

        accuracy = accuracy_score(
            y_test,
            predictions
        )

        # Log parameters
        mlflow.log_params(params)

        # Log metric
        mlflow.log_metric(
            "accuracy",
            accuracy
        )

        # Log model
        mlflow.sklearn.log_model(
            model,
            name="model",
            skops_trusted_types=[
                "sklearn.tree._tree.Tree"
            ]
        )

        print(
            f"Run: {run.info.run_id} | "
            f"n_estimators={params['n_estimators']} | "
            f"max_depth={params['max_depth']} | "
            f"accuracy={accuracy:.4f}"
        )

        # Track best model
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_run_id = run.info.run_id


# ==========================================
# DISPLAY BEST RESULT
# ==========================================

print("\n==========================================")
print("BEST MODEL")
print("==========================================")

print(f"Best Accuracy: {best_accuracy:.4f}")
print(f"Best Run ID: {best_run_id}")

print("\n5 experiments completed successfully.")