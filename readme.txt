  # Quality Control Defect Prediction 

  # Project Purpose
This project aims to predict whether an item is defective based on multiple features using a machine learning model.
 The goal is to improve the quality control process in manufacturing by identifying defective items early and reducing costs.

1. Clone the Repository

To get started with the project, clone the repository to your local machine using the following commands:
git clone https://github.com/Saronzeleke/QUALITY-CONTROL-.git
cd QUALITY-CONTROL


2. Install Dependencies

Ensure you have Python, ancanoda or jupyter notebook installed on your machine. 
Install the required dependencies using the provided requirements.txt file:
pip install -r requirements.txt


3. Run the FastAPI Server

To run the FastAPI server:
uvicorn quality:app --reload
The server will start on http://127.0.0.1:8000.
 
Send the POST request using curl:
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d @input_data.json

#Contact

For any questions or issues, please contact sharonkuye369@gmail.com.