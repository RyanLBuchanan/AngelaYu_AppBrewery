import os

import requests
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

MY_LAT = 41.222759
MY_LONG = -111.970421

MY_API_KEY = os.getenv("API_KEY")

PARAMETERS = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": MY_API_KEY,
}

"""
Complete API with parameters and my API key:
https://api.openweathermap.org/data/3.0/onecall?lat=41.222759&lon=-111.970421&appid=MY_API_KEY
"""

response = requests.get("https://api.openweathermap.org/data/3.0/onecall", params=PARAMETERS)
response.raise_for_status()
data = response.json()
print(data)