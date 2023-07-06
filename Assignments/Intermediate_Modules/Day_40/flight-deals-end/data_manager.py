import os
from dotenv import load_dotenv
import requests

load_dotenv()

# Constants
# Sheety API constants
SHEETY_ENDPOINT_KEY = os.environ["SHEETY_ENDPOINT_KEY"]
PROJECTNAME = "flightDeals"
SHEETNAME = "prices"
SHEETY_BASIC_USERNAME = os.environ["SHEETY_BASIC_USERNAME"]
SHEETY_PRICES_ENDPOINT = f"https://api.sheety.co/{SHEETY_BASIC_USERNAME}/{PROJECTNAME}/{SHEETNAME}"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)