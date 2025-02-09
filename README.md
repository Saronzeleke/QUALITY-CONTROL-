Quality Control Defect Prediction
 # Project Purpose

This project aims to predict whether an item is defective based on multiple features using a machine learning model. The goal is to improve the quality control process in manufacturing by identifying defective items early and reducing costs.
Setup Instructions
1. Clone the Repository
 # git clone https://github.com/Saronzeleke/QUALITY-CONTROL-.git

2. Install Dependencies
 # pip install -r requirements.txt

3. Run the FastAPI Server
 # python -m uvicorn quality:app --reload

Usage
Making Predictions

Send a POST request to the /predict endpoint with the feature data.
Example Request

Save the input data as input_data.json:
{
    "feature1": 0.5,
    "feature2": 1.2,
    "feature3": 3.1,
    "feature4": 4.0,
    "feature5": 0.1,
    "feature6": 2.3,
    "feature7": 1.5,
    "feature8": 0.7,
    "feature9": 2.8,
    "feature10": 3.0,
    "feature11": 1.1,
    "feature12": 0.9,
    "feature13": 2.0,
    "feature14": 3.5,
    "feature15": 0.8,
    "feature16": 1.4,
    "feature17": 2.6,
    "feature18": 1.0,
    "feature19": 3.3,
    "feature20": 2.1,
    "feature21": 0.4,
    "feature22": 1.8,
    "feature23": 2.7,
    "feature24": 3.6,
    "feature25": 0.3,
    "feature26": 1.7,
    "feature27": 2.5,
    "feature28": 3.4,
    "feature29": 0.2,
    "feature30": 1.9
}


Send the POST request using curl:
 # curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d @input_data.json

 # API Documentation

FastAPI automatically generates interactive API documentation. You can access it at:

1. Onrender.com/docs (https://quality-control-1.onrender.com/) - Write https://quality-control-1.onrender.com/docs and then click the execute button
2. Swagger UI: http://127.0.0.1:8000/docs
3. ReDoc: http://127.0.0.1:8000/redoc
Project Structure

quality.py: The main FastAPI application file.
quality_control_data.csv: The synthetic dataset used for training the model.
best_model.joblib and scaler.joblib: Saved model and scaler files.
requirements.txt: A list of dependencies required for the project.
input_data.json: Example input data for making predictions.

 # Contact

For any questions or issues, please contact sharonkuye369@gmail.com.

