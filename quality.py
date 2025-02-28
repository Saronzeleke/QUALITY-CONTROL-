from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
import os 
import uvicorn
app = FastAPI()

# Load the trained model and scaler
try:
    model = joblib.load('best_model.joblib')
    scaler = joblib.load('scaler.joblib')
except Exception as e:
    raise HTTPException(status_code=500, detail=f"Failed to load model or scaler: {str(e)}")

class InputData(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    feature4: float
    feature5: float
    feature6: float
    feature7: float
    feature8: float
    feature9: float
    feature10: float
    feature11: float
    feature12: float
    feature13: float
    feature14: float
    feature15: float
    feature16: float
    feature17: float
    feature18: float
    feature19: float
    feature20: float
    feature21: float
    feature22: float
    feature23: float
    feature24: float
    feature25: float
    feature26: float
    feature27: float
    feature28: float
    feature29: float
    feature30: float

@app.post("/predict")
async def predict(input_data: InputData):
    try:
        # Convert input data to DataFrame
        data_dict = input_data.dict()
        input_df = pd.DataFrame([data_dict])

        # Check for missing features
        if input_df.isnull().values.any():
            raise HTTPException(status_code=400, detail="Missing features in the input data")

        # Scale the input data
        try:
            input_df = scaler.transform(input_df)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error in scaling input data: {str(e)}")

        # Make prediction
        try:
            prediction = model.predict(input_df)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error in making prediction: {str(e)}")

        return {"prediction": prediction.tolist()}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
   

    port = int(os.getenv("PORT", 8000)) 
    uvicorn.run(app, host="0.0.0.0", port=port)

