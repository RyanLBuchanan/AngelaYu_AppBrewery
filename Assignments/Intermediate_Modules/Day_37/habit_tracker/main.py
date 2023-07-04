import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()

# FOR CREATING PIXELA USER
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "rylobuchanan"
GRAPHID = "graph1"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
POST_PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPHID}"

today = datetime.now()

UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"

PIXELA_TOKEN = os.environ['PIXELA_TOKEN']

user_params = {
    "token": PIXELA_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Graph parameters
graph_config = {
    "id": GRAPHID,
    "name": "Python Programming Graph",
    "unit": "hours",
    "type":  "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "4"
}

# Delete pixel
# response = requests.delete(url=UPDATE_ENDPOINT, headers=headers)
# print(response.text)

# Update pixels with put method
# response = requests.put(url=UPDATE_ENDPOINT, json=pixel_data, headers=headers)
# print(response.text)

# Post a pixel to the Python Programming Graph
response = requests.post(url=POST_PIXEL_ENDPOINT, json=pixel_data, headers=headers)
print(response.text)

# Create Python Programming Graph
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

# Create Pixela username and token
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)