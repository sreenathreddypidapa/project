from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd

# Load the saved model
model = joblib.load("logistic_model.pkl")

# Initialize FastAPI app
app = FastAPI()
@app.get("/")
def home():
    return {"message": "API is up and running"}

@app.post("/predict/")
def predict(data: dict):
    try:
        # Convert input data to a DataFrame
        input_data = pd.DataFrame([data])

        # Perform prediction
        prediction = model.predict(input_data)
        return {"prediction": int(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))