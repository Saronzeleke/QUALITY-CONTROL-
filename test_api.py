import requests
import json

url = "http://127.0.0.1:8000/predict"  # Change this if deployed
headers = {"Content-Type": "application/json"}

with open("test_input.json", "r") as file:
    data = json.load(file)

response = requests.post(url, json=data, headers=headers)
print(response.json())
