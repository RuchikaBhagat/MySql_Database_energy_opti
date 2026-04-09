import requests

url = "http://127.0.0.1:5000/ingest"

data = {
    "device_id": 1,
    "voltage": 230,
    "current": 5,
    "power": 1150,
    "energy": 1.2,
    "frequency": 50,
    "power_factor": 0.95
}

response = requests.post(url, json=data)

print("Response:", response.text)