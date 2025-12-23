from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PredictionRequest(BaseModel):
    home_team: str
    away_team: str

@app.get("/")
def root():
    return {"status": "Predictor API running"}

@app.post("/predict")
def predict(data: PredictionRequest):
    return {
        "prediction": "Home Win",
        "confidence": 70
    }
