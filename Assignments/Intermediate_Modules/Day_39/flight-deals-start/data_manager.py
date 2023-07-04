import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()

# Constants
# Sheety API constants
SHEETY_ENDPOINT_KEY = os.environ["SHEETY_ENDPOINT_KEY"]
PROJECTNAME = "flightDeals"
SHEETNAME = "prices"
SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_ENDPOINT_KEY}/{PROJECTNAME}/{SHEETNAME}"
SHEETY_BASIC_USERNAME = os.environ["SHEETY_BASIC_USERNAME"]
SHEETY_BASIC_PASSWORD = os.environ["SHEETY_BASIC_PASSWORD"]

# Kiwi API constants
KIWI_HEADERS = os.environ["KIWI_HEADERS"]
KIWI_ENDPOINT = os.environ["KIWI_ENDPOINT"]
KIWI_API_KEY = os.environ["KIWI_API_KEY"]

kiwi_parameters = {

}

today = datetime.now()
class DataManager:

    def __init__(self):

        # Retrieve prices with Kiwi.com API
        kiwi_response = requests.get(url=KIWI_ENDPOINT, json=kiwi_parameters, headers=KIWI_HEADERS)
        kiwi_response.raise_for_status()
        price_result = kiwi_response.json()
        print(price_result)

        #This class is responsible for talking to the Google Sheet.
        for price in price_result["exercises"]:
            sheet_inputs = {
                "workout": {
                    "city": "",
                    "iata code": "",
                    "lowest price": 0
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