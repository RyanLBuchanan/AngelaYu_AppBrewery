import os
from datetime import datetime

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

USERNAME = os.environ["SHEETY_USERNAME"]
PROJECTNAME = "myWorkouts"
SHEETNAME = "workouts"
SHEETY_ENDPOINT = f"https://api.sheety.co/{USERNAME}/{PROJECTNAME}/{SHEETNAME}"
SHEETY_BASIC_USERNAME = os.environ["SHEETY_BASIC_USERNAME"]
SHEETY_BASIC_PASSWORD = os.environ["SHEETY_BASIC_PASSWORD"]

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

nix_response = requests.post(url=NIX_EXERCISE_ENDPOINT, json=post_request_body, headers=HEADERS)
nix_response.raise_for_status()
workout_result = nix_response.json()
print(workout_result)

today = datetime.now()

for exercise in workout_result["exercises"]:
    sheet_inputs = {
        "workout" : {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

# Basic authentication
sheety_response = requests.post(
    url=SHEETY_ENDPOINT,
    json=sheet_inputs,
    auth=(SHEETY_BASIC_USERNAME,
          SHEETY_BASIC_PASSWORD
    )
)

sheety_response.raise_for_status()
print(sheety_response.text)
