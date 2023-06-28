import pandas as pd
import smtplib
import datetime as dt
import random

MY_EMAIL = "ryan.py.test@gmail.com"
MY_PASSWORD = "cobcghtixdcgimey"
INPUT_FILE = "quotes.txt"

now = dt.datetime.now()
day_of_week = now.weekday()


if day_of_week == 2:
    # Read quotes in from the text file
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
#
#
#
# # year = now.year
# #
# # day_of_week = now.weekday()
# #
# # if day_of_week == 2:
#
# # date_of_birth = dt.datetime(year=1974, month=6, day=4, hour=3)
#
# # connection.close()
