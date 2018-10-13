'''
Written by Michelle Lim Shi Hui & Nicholas Phang
Dean's Crisis Management System - Notification Subsystem
For CZ3003 Software System Analysis & Design

Email Manager -
Takes in email address list & message, formats it, and sends out the email
Leverages on smtplib
'''

import smtplib
import oauth_creds

def main(data, emailList):
    sent_from = oauth_creds.gmail_user
    to = emailList #['email','email']
    subject = "Crisis Management Summary Report"
    body = data
    email_text = """ 
    From: %s  
    To: %s  
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server_ssl.ehlo()
        server_ssl.login(oauth_creds.gmail_user, oauth_creds.gmail_password)
        print('Connection to Gmail Success!')
        server_ssl.sendmail(sent_from, to, email_text)
        server_ssl.close()
        print('Email sent!')
    except:
        print('Something went wrong...')

