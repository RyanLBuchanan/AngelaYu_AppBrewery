import smtplib
import requests
from datetime import datetime
import time
import os
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

MY_LAT = 41.222759
MY_LONG = -111.970421

"""LONDON COORDINATES"""
# MY_LAT = 51.507351 # Your latitude
# MY_LONG = -0.127758 # Your longitude


# If the ISS is close to my current position
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # iss_position = (iss_longitude, iss_latitude)
    # print(iss_position)

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


# and it is currently dark
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


# Then email me to tell me to look up.
while True:
    # BONUS: run the code every 60 seconds.
    time.sleep(60)
    if is_iss_overhead() and is_night():

        # Email me notification
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="buchanan.ryan22@gmail.com",
                msg="Subject: Don't Look Up, TURD!\n\nThe ISS is above you.  Maybe you can see it!"
            )

