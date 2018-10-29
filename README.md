# Dean's Crisis Management System - Notification Subsystem
> This subsystem takes a message from the API subsystem, parses it, and redirects it to the relevant destination: Email, WhatsApp, or Facebook & Twitter. 


## How to Start

Windows:

1. Clone the repository
```sh
git clone git://github.com/Deans-CMS/deans-notification.git
```

2. Install dependencies
```sh
pip install-r requirements.txt
```

3. Start server (the API server will start on 	**localhost:8000**)
```sh
python message_manager.py
```

4. Set up Twilio

As WhatsApp for Twilio is still in Sandbox mode, please connect your WhatsApp number to Sandbox to receive messages through Twilio.
> Send a WhatsApp message to **+1 415 523 8886** with the code ```join coquelicot-labradoodle```.

## API Endpoints

1. Facebook & Twitter ```/socialmessages/```
```sh
POST /socialmessages/ HTTP/1.1
Host: 127.0.0.1
Content-Type: application/json
cache-control: no-cache
Postman-Token: 2f604143-450a-45e9-bf85-a5442d3173b0
{"message" : "hello world!"}
```

2. WhatsApp ```/dispatchnotices/```
```sh
POST /dispatchnotices/ HTTP/1.1
Host: 127.0.0.1
Content-Type: application/json
cache-control: no-cache
Postman-Token: fde35f4e-0cd6-4178-8b13-65c274d0bb9b
{"number":"+6586830963","message":"URGENT: Fire @ 38 Nanyang Cres, Singapore 636866. Block 24 #06-120."}
```

3. Email Reports ```/reports/```

TO BE UPDATED

## Accounts:

Email account: deanscms@gmail.com

Facebook Page: https://www.facebook.com/deans.cms/ 

Twitter Account: https://twitter.com/dean_cms
