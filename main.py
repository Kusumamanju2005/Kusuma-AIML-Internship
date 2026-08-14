
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(title="Breast Cancer Prediction API")

# Load trained model
model = joblib.load("breast_cancer_model.joblib")


class PredictionRequest(BaseModel):
    features: list[float]


@app.get("/")
def home():
    return {
        "message": "Breast Cancer Prediction API is running"
    }


@app.post("/predict")
def predict(request: PredictionRequest):

    input_data = pd.DataFrame([request.features])

    prediction = int(model.predict(input_data)[0])
    confidence = float(model.predict_proba(input_data).max())

    return {
        "prediction": prediction,
        "confidence": round(confidence, 4)
    }
