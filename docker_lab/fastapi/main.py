from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

model = pickle.load(open("wine_model.pkl", "rb"))

@app.get("/")
def home():
    return {"message": "Wine API running"}

@app.post("/predict")
def predict(data: dict):
    features = np.array(data["features"]).reshape(1, -1)
    prediction = model.predict(features)
    return {"prediction": int(prediction[0])}
