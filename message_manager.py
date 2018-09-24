'''
Written by Michelle Lim Shi Hui & Nicholas Phang
Dean's Crisis Management System - Notification Subsystem
For CZ3003 Software System Analysis & Design

Message Manager -
Main function that receives & processes the messages received from API subsystem, calls the relevant API endpoints
'''

# PSEUDOCODE FIRST, WILL DO THE ACTUAL CODING LATER.

# imports the 4 subfiles
import email_client
import facebook_client
import sms_client
import twitter_client

# if __name__ == "__main__":

#############################################
#       CONNECTION TO API SUBSYSTEM         #
############################W#################

# listener, polls for events
# on trigger, parse message

#############################################
#             MESSAGE PARSING               #
#############################################

# Questions:
# 1) what is the message format that will be delivered to us?
# 2) what will be contained in the message?
# 3) need some system such that we know what kind of message it is
#       1) crisis signal 2) summary report 3) social message

#############################################
#            MESSAGE REDIRECTING            #
#############################################

# if type = crisis signal:
#   sms_api.connect(twilio_credentials)
#   sms_api.format(message)
#   sms_api.post(sms_list)

# if type = summary_report:
#   email_api.connect(email_credientials)
#   email_api.format(message)
#   email_api.post(email_add_list)

# if type = social_message:
#   facebook_api.connect(facebook_credientials)
#   facebook_api.format(message)
#   facebook_api.post()
#   twitter_api.connect(ckey, csecret, akey, asecret)
#   twitter_api.format(message)
#   twitter_api.post()




