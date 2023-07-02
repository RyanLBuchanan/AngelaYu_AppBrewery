import os
from dotenv import load_dotenv
import requests

load_dotenv()

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_TOKEN = os.environ['PIXELA_TOKEN']

user_params = {
    "token": PIXELA_TOKEN,
    "username": "rylobuchanan",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create Pixela username and token
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)