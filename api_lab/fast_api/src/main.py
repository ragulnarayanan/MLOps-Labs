from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from .predict import predict_data

app = FastAPI()

class WineFeatures(BaseModel):
    alcohol: float
    malic_acid: float
    alcalinity_of_ash: float
    flavanoids: float
    nonflavanoid_phenols: float
    color_intensity: float

class WinePredictionResponse(BaseModel):
    predicted_class: int

@app.get("/", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "Wine API is up!"}

@app.post("/predict", response_model=WinePredictionResponse)
async def predict_wine_class(features: WineFeatures):
    try:
        data = [[
            features.alcohol,
            features.malic_acid,
            features.alcalinity_of_ash,
            features.flavanoids,
            features.nonflavanoid_phenols,
            features.color_intensity
        ]]
        prediction = predict_data(data)
        return WinePredictionResponse(predicted_class=int(prediction[0]))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))