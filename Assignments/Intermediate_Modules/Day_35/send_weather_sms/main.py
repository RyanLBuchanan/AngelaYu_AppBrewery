import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client

load_dotenv()  # Load environment variables from .env file

# Twilio dashboard information
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

# Latitude and longitude constants for Ogden, Utah, USA
MY_LAT = 41.222759
MY_LONG = -111.970421

# Latitude and longitude constants for Palm Beach, Florida, USA
WEST_PALM_BEACH_FL_LAT = 26.714439
WEST_PALM_BEACH_FL_LONG = -80.054947

# Latitude and longitude constants for Puerto Galera, Philippines
PUERTO_GALERA_LAT = 13.501690
PUERTO_GALERA_LONG = 120.955101

# Open Weather One Call API endpoint
OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"

# Import environment variables from .env file
API_KEY = os.getenv("API_KEY")
ONE_CALL_API_KEY = os.getenv("ONE_CALL_API_KEY")

# Optional parameters
PART = "current,minutely,daily"

PARAMETERS = {
    "lat": PUERTO_GALERA_LAT,
    "lon": PUERTO_GALERA_LONG,
    "exclude": PART,
    "appid": ONE_CALL_API_KEY,
}

response = requests.get(OWM_Endpoint, params=PARAMETERS)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
# print(weather_slice)
# print(weather_data["hourly"][0]["weather"][0]["id"])

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_="+18554760916",
        to="+13854329281"
    )
    print(message.status)

