import pandas as pd
import smtplib
import datetime as dt
import random
import time
import os
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

INPUT_FILE = "quotes.txt"

# Loop indefinitely
while True:
    now = dt.datetime.now()
    day_of_week = now.weekday()

    if day_of_week == 2:
        # Read quotes from the text file
        with open(INPUT_FILE, "r") as file:
            all_quotes = file.readlines()
            quote = random.choice(all_quotes)

        print(quote)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="buchanan.ryan22@gmail.com",
                msg=f"Subject:Morning Inspiration\n\n{quote}"
            )

    # Delay for 24 hours before executing the code again
    time.sleep(24 * 60 * 60)
