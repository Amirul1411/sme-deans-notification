'''
Written by Michelle Lim Shi Hui & Nicholas Phang
Dean's Crisis Management System - Notification Subsystem
For CZ3003 Software System Analysis & Design

WhatsApp API -
Takes in a message & sends as a WhatsApp message
Leverages on Twilio package
'''

from twilio.rest import Client

#Get API keys
from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')
account_sid = config.get('twilio', 'account_sid')
token = config.get('twilio', 'token')

def main(data):
    client = Client(account_sid, token)
    print('Twilio Connection Successful')
    post(client, data)
    print('Whatsapp Message Sent')

def post(client, data):
    message = client.messages.create(
        to="whatsapp:+6586830963",
        from_="whatsapp:+14155238886",
        body=data)
    print(message.sid)