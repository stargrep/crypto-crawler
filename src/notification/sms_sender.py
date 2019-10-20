# we import the Twilio client from the dependency we just installed
from twilio.rest import Client


def send_sms(msg):
    # the following line needs your Twilio Account SID and Auth Token
    client = Client("AC", "")

    # change the "from_" number to your Twilio number and the "to" number
    # to the phone number you signed up for Twilio with, or upgrade your
    # account to send SMS to any phone number
    client.messages.create(to="+13479560550",
                           from_="+12064832138",
                           body=msg)
