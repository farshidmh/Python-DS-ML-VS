import requests
import json

# Make sure it matches your engine
url = 'http://127.0.0.1:5000/predict'

data = {
    "age": 25,
    "gender": "Female"
}

response = requests.post(
    url,
    data=json.dumps(data),
    headers={'Content-Type': 'application/json'}
)

print(response.json())
