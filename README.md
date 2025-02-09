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

