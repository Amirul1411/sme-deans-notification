'''
Written by Michelle Lim Shi Hui & Nicholas Phang
Dean's Crisis Management System - Notification Subsystem
For CZ3003 Software System Analysis & Design

Facebook API -
Takes in Facebook credentials & message, formats the message & posts it
Leverages on Facebook's Graph API
'''

import facebook
import oauth_creds

def main(data):
    cfg = {
        "page_id": 2189340524616954,
        "access_token": oauth_creds.fb_accesstoken
    }

    api = get_api(cfg)
    print('Facebook Connection Successful')
    status = api.put_wall_post(data)

def get_api(cfg):
    graph = facebook.GraphAPI(cfg['access_token'])
    # Get page token to post as the page. You can skip
    # the following if you want to post as yourself.
    resp = graph.get_object('me/accounts')
    page_access_token = None
    for page in resp['data']:
        if page['id'] == cfg['page_id']:
            page_access_token = page['access_token']
            graph = facebook.GraphAPI(page_access_token)
            return graph