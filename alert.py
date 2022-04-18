import dotenv
import sys
import os
from dotenv import load_dotenv
from twilio.rest import Client

# Credentials
load_dotenv()

TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_AUTH = os.getenv('TWILIO_AUTH')
TWILIO_NUMBER = os.getenv('TWILIO_NUMBER')

client = Client(
    TWILIO_SID, 
    TWILIO_AUTH
)

def send_alert():
    msg = client.messages.create(
        to="+918452861970",
        from_=TWILIO_NUMBER,
        body="UPDATE: Accident detected",
    )