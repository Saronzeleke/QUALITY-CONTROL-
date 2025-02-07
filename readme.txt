 Quality Control Defect Prediction 

 Project Purpose
This project aims to predict whether an item is defective based on multiple features using a machine learning model.
 The goal is to improve the quality control process in manufacturing by identifying defective items early and reducing costs.

1. Clone the Repository

To get started with the project, clone the repository to your local machine using the following commands:
git clone https://github.com/Saronzeleke/QUALITY-CONTROL-.git
cd QUALITY-CONTROL


2. Install Dependencies

Ensure you have Python installed on your machine. 
Install the required dependencies using the provided requirements.txt file:
pip install -r requirements.txt


3. Run the FastAPI Server

To serve the machine learning model and create an API for predictions, run the FastAPI server:
uvicorn quality:app --reload
The server will start on http://127.0.0.1:8000.
Usage
Making Predictions

To make predictions using the API, send a POST request to the /predict endpoint with the feature data.
Example Request

Save the following JSON data as input_data.json:
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


