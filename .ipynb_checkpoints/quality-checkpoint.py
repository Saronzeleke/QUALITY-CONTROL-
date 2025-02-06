from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib

app = FastAPI()

# Load the trained model and scaler
model = joblib.load('best_model.joblib')
scaler = joblib.load('scaler.joblib')

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
        
        # Scale the input data
        input_df = scaler.transform(input_df)
        
        # Make prediction
        prediction = model.predict(input_df)
        
        return {"prediction": prediction.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


