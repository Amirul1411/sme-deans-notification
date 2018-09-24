'''
Written by Michelle Lim Shi Hui & Nicholas Phang
Dean's Crisis Management System - Notification Subsystem
For CZ3003 Software System Analysis & Design

Twitter API -
Takes in twitter credentials & message, formats the message & posts it
Leverages on Tweepy package to connect to Twitter API endpoint
'''

import tweepy

def connect (ckey,csecret,akey,asecret):
    consumer_key = ckey
    consumer_secret = csecret
    access_key = akey
    access_secret = asecret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    api.update_status('Twitter Authentication Complete')

def format_message (message):
    # TODO: format message here

def post():
    # TODO: post message here