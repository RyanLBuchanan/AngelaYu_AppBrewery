import os
from dotenv import load_dotenv
import requests

load_dotenv()

# Constants
GENDER = "male"
WEIGHT = 82
HEIGHT = 180
AGE = 49


NIX_APP_ID = os.environ["NIX_APP_ID"]
NIX_API_KEY = os.environ["NIX_API_KEY"]

NIX_EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"


HEADERS = {
    "x-app-id": NIX_APP_ID,
    "x-app-key": NIX_API_KEY,
    # "x-remote-user-id": "0"
}

exercise_input = input("Tell me which exercises you did: ")

post_request_body = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=NIX_EXERCISE_ENDPOINT, json=post_request_body, headers=HEADERS)
response.raise_for_status()
result = response.json()
print(result)