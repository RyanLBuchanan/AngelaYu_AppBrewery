import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client
from datetime import datetime

load_dotenv()

# Twilio dashboard information
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self):

        self.prices = []

        self.price = price
        self.city = city
        self.aita = aita

        self.today = datetime.now()
        self.return_date = datetime.now() + datetime.timedelta()


        # Create a new list of the city-airport and prices using list comprehension.
        self.formatted_price_updates = [f"Low price alert! Only ${self.price} to fly from {self.city}-{self.aita} from {self.today.strftime('%Y-%m-%d')} to {self.return_date.strftime('%Y-%m-%d')}." for price in prices]


    def send_notification(self):
        # Send each article as a separate message via Twilio.
        client = Client(account_sid, auth_token)
        for price in self.formatted_price_updates:
            message = client.messages \
                .create(
                body=price,
                from_="+18554760916",
                to="+13854329281"
            )
            print(message.status)