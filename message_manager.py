'''
Written by Michelle Lim Shi Hui & Nicholas Phang
Dean's Crisis Management System - Notification Subsystem
For CZ3003 Software System Analysis & Design

Message Manager -
Main function that receives & processes the messages received from API subsystem, calls the relevant API endpoints
'''

#imports the 4 subfiles
import email_client
import facebook_client
import sms_client
import twitter_client

# if __name__ == "__main__":

#############################################
#       CONNECTION TO API SUBSYSTEM         #
############################W#################

# listener, polls for events
# onEvent, add message to queue

#############################################
#             MESSAGE PARSING               #
#############################################

# Questions:
# 1) what is the message format that will be delivered to us?
# 2) what will be contained in the message?
# 3) need some system such that we know what kind of message it is
#       1) crisis signal 2) summary report 3) social message

#sample message:
message = 'r, fire at 639798, 865' #message type, message data, message number/credentials
messageList = [x.strip() for x in message.split(',')]
type = messageList[0]
data = messageList[1]
dest = messageList[2]

emailList = ['michellelimsh@gmail.com']
#############################################
#            MESSAGE REDIRECTING            #
#############################################

#message type = c for crisis, r for report, s for social media

if type == 'c':
    print('Connecting to Twilio...')
    sms_client.main(data)

if type == 'r':
    print('Connecting to Gmail...')
    email_client.main(data, emailList)

if type == 's':
    print('Connecting to Twitter...')
    twitter_client.main(data)
    print('Connecting to Facebook...')
    facebook_client.main(data)




