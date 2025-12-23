from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PredictionRequest(BaseModel):
    home_team: str
    away_team: str

@app.get("/")
def root():
    return {"status": "Predictor API running"}

def normalize(team: str):
    return team.strip().lower()

BIG_TEAMS = {
    "arsenal", "chelsea", "man city", "manchester city",
    "man united", "manchester united", "liverpool",
    "real madrid", "barcelona", "bayern munich",
    "psg", "juventus"
}

@app.post("/predict")
def predict(data: PredictionRequest):
    home = normalize(data.home_team)
    away = normalize(data.away_team)

    home_score = 1.2
    away_score = 1.0

    if home in BIG_TEAMS:
        home_score += 0.5
    if away in BIG_TEAMS:
        away_score += 0.5

    diff = home_score - away_score

    if abs(diff) < 0.3:
        prediction = "Draw"
        confidence = 55
    elif diff > 0:
        prediction = "Home Win"
        confidence = min(80, int(60 + diff * 15))
    else:
        prediction = "Away Win"
        confidence = min(80, int(60 + abs(diff) * 15))

    return {
        "prediction": prediction,
        "confidence": confidence
    }
