'''
Written by Michelle Lim Shi Hui & Nicholas Phang
Dean's Crisis Management System - Notification Subsystem
For CZ3003 Software System Analysis & Design

Email Manager -
Takes in email address list & message, formats it, and sends out the email
Leverages on smtplib
'''

import smtplib

#Get API keys
from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')
user = config.get('gmail', 'user')
password = config.get('gmail', 'password')

def main(emailadd, subject, report):
    sent_from = user
    to = emailadd
    subject = subject
    email_text = """ 
    Dear President,
    
    This is the report for ## date ##time. 
    
    Best Regards,
    Dean's Crisis Management Service
    
    This is an auto-generated message. Please do not reply.
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server_ssl.ehlo()
        server_ssl.login(user, password)
        print('Connection to Gmail Success!')
        server_ssl.sendmail(sent_from, to, email_text)
        server_ssl.close()
        print('Email sent!')
    except:
        print('Something went wrong...')

