from datetime import datetime
import pandas as pd
import smtplib
import random
import time
import os
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

# Loop indefinitely
while True:
    TODAY = datetime.now()
    TODAY_TUPLE = (TODAY.month, TODAY.day)

    data = pd.read_csv("birthdays.csv")
    birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

    if TODAY_TUPLE in birthdays_dict:
        birthday_person = birthdays_dict[TODAY_TUPLE]
        file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(file_path) as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", birthday_person["name"])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="buchanan.ryan22@gmail.com",
                msg=f"Subject:Happy Birthday, TURD!\n\n{contents}"
            )

    # Delay for 24 hours before executing the code again
    time.sleep(24 * 60 * 60)
