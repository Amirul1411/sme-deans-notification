'''
Written by Michelle Lim Shi Hui & Nicholas Phang
Dean's Crisis Management System - Notification Subsystem
For CZ3003 Software System Analysis & Design

Email Manager -
Takes in email address list & message, formats it, and sends out the email
Leverages on smtplib
'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

#Get API keys
from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')
user = config.get('gmail', 'user')
password = config.get('gmail', 'password')

def main(emailadd, subject, report):
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = emailadd
    msg['Subject'] = subject
    body = """ 
    Dear President,
    
    This is the report for %s. 
    
    Best Regards,
    Dean's Crisis Management Service
    
    This is an auto-generated message. Please do not reply.
    """ % (datetime.now().strftime("%I:%M%p on %B %d, %Y"))
    msg.attach(MIMEText(body, 'plain'))

    filename = report
    attachment = open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= "+filename[filename.index("/")+1:])

    msg.attach(part)

    text = msg.as_string()

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(user, password)
        print('Connection to Gmail Success!')
        server.sendmail(user, emailadd, text)
        server.quit()
        print('Email sent!')
    except:
        #TODO: Exception Handling
        print('Something went wrong...')

