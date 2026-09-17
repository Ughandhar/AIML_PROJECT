from fastapi import FastAPI
from pydantic import BaseModel
import joblib

loaded_model = joblib.load("notebooks/logistic_model_fastapi.pkl")

app = FastAPI(title="ML Model Serving API")


class PredictionInput(BaseModel):
    hours_studied: float
    exam_score: float


@app.get("/")
def home():
    return {"message": "ML Model Serving API is running"}


@app.post("/predict")
def predict(data: PredictionInput):
    features = [[data.hours_studied, data.exam_score]]
    prediction = loaded_model.predict(features)[0]

    return {
        "prediction": int(prediction),
        "passed": bool(prediction)
    }