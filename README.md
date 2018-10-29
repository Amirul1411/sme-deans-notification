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

3. Start server
```sh
python message_manager.py
```
The API server will start on 127.0.0.1:8000

## API Endpoints

1. Sending message to Facebook & Twitter
```sh
POST /socialmessages/ HTTP/1.1
Host: 127.0.0.1
Content-Type: application/json
cache-control: no-cache
Postman-Token: 2f604143-450a-45e9-bf85-a5442d3173b0
{"message" : "hello world!"}
```

2. Sending dispatch announcement through WhatsApp

TO BE UPDATED


3. Generating a Jasper Report & Sending through Email

TO BE UPDATED

## Links:

Email account: deanscms@gmail.com

Facebook Page: https://www.facebook.com/deans.cms/ 

Twitter Account: https://twitter.com/dean_cms
