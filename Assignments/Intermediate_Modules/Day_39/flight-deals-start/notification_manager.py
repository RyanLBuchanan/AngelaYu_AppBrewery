import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

# Twilio dashboard information
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.client = Client(account_sid, auth_token)


    def send_sms(self, message):
        # Send each article as a separate message via Twilio.
        message = self.client.messages.create(
            body=message,
            from_="+18554760916",
            to="+13854329281"
            )
        print(message.sid)