import requests
from datetime import datetime
import pandas as pd
import smtplib
import time
import os
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

MY_LAT = 41.222759
MY_LONG = -111.970421

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

# Request sunrise and sunset data
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

# International Space Station API
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)
print(iss_position)

while True:

    #If the ISS is close to my current position
    if time_now < sunrise or time_now > sunset and iss_position == (MY_LONG, MY_LAT):
        # Email me notification
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="buchanan.ryan22@gmail.com",
                msg=f"Subject: Don't Look Up, TURD!\n\nThe ISS is at {iss_position}.  Maybe you can see it!"
            )

    # Delay for 60 seconds before executing the code again
    time.sleep(60)