'''
Written by Michelle Lim Shi Hui & Nicholas Phang
Dean's Crisis Management System - Notification Subsystem
For CZ3003 Software System Analysis & Design

Twitter API -
Takes in twitter credentials & message, formats the message & posts it
Leverages on Tweepy package to connect to Twitter API endpoint
'''

import tweepy
import oauth_creds

def main(data):
    auth = tweepy.OAuthHandler(oauth_creds.ckey, oauth_creds.csecret)
    auth.set_access_token(oauth_creds.atoken, oauth_creds.asecret)
    print('Twitter Authentication Complete')
    api = tweepy.API(auth)
    post(api, data)

def post(api, data):
    api.update_status(data)
    print(data)
    print("Twitter Post Successful")

