 Quality Control Defect Prediction 

  # Project Purpose
This project aims to predict whether an item is defective based on multiple features using a machine learning model.
 The goal is to improve the quality control process in manufacturing by identifying defective items early and reducing costs.

1. Clone the Repository

To get started with the project, clone the repository to your local machine using the following commands:
git clone https://github.com/Saronzeleke/QUALITY-CONTROL-.git

2. Install Dependencies

Ensure you have Python, ancanoda or jupyter notebook installed on your machine. 
Install the required dependencies using the provided requirements.txt file:
 # pip install -r requirements.txt
3. Run the FastAPI Server

To run the FastAPI server:
 python -m uvicorn quality:app --reload
The server will start on http://127.0.0.1:8000.
 
 # Send the POST request using curl:
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d @input_data.json
 # To open the deployed link just go to the  https://quality-control-1.onrender.com then write https://quality-control-1.onrender.com/docs    
 it take you to Fastapi site then just click the defualt it shows the selection then click Try it out  then click the execute button then it shows the prediction.

#Contact

For any questions or issues, please contact sharonkuye369@gmail.com.
