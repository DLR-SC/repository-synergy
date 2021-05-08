Canarytokens
=============
by Thinkst Applied Research

Overview
--------
Canarytokens helps track activity and actions on your network.

Installation
------------
We recommend [the Docker image installation process](https://github.com/thinkst/canarytokens-docker).

Configuration
-------------

The Canarytokens server can use many different settings configurations. You can find them in `settings.py`. There are two
main settings files: `frontend.env` and `switchboard.env`. 

The `frontend.env` contains the frontend process settings such as:
- CANARY_DOMAINS=mytesttokensdomain.com
- CANARY_NXDOMAINS=pdf.demo.canarytokens.net
- CANARY_AWSID_URL=<custom awsid url>
- CANARY_WEB_IMAGE_UPLOAD_PATH=/uploads
- CANARY_GOOGLE_API_KEY=<custom google maps api key>
- LOG_FILE=frontend.log

The `switchboard.env` contains the switchboard process settings such as:
- CANARY_MAILGUN_DOMAIN_NAME=<mailgun domain>
- CANARY_MAILGUN_API_KEY=
- CANARY_MANDRILL_API_KEY=
- CANARY_SENDGRID_API_KEY=
- CANARY_PUBLIC_IP=<instead of using a domain>
- CANARY_PUBLIC_DOMAIN=<instead of using an IP>
- CANARY_ALERT_EMAIL_FROM_ADDRESS=noreply@yourdomain.com
- CANARY_ALERT_EMAIL_FROM_DISPLAY="Canarytoken Mailer"
- CANARY_ALERT_EMAIL_SUBJECT="Alert"
- CANARY_SMTP_USERNAME=<smtp username>
- CANARY_SMTP_PASSWORD=<smtp password>
- CANARY_SMTP_SERVER=smtp.gmail.com
- CANARY_SMTP_PORT=587
- CANARY_WEB_IMAGE_UPLOAD_PATH=/uploads
- LOG_FILE=switchboard.log

Please note that when choosing which email provider you would like to use, you **MUST** only provide
information related to that provider. E.g. if you have `CANARY_MAILGUN_API_KEY` then you must remove the others such as
`CANARY_SENDGRID_API_KEY` and `CANARY_MANDRILL_API_KEY`. 

Lastly, we have added the ability to specify your own AWSID lambda so that you may host your own. The setting is placed in
`frontend.env` under `CANARY_AWSID_URL`. If this value is not specified, it will use our default hosted lambda. 

### Configuration of Outgoing SMTP
When configuring outgoing SMTP please consider the following:

Restrictions:
* no other provider like Mailgun or Sendgrid must be configured for this to work
* only supports StartTLS right now (you have to use the corresponding port)
* no anonymous SMTP supported right now (you have to use username/password to authenticate)

The following settings have to be configured in `switchboard.env` for SMTP to work:
* CANARY_SMTP_SERVER: the SMTP server
* CANARY_SMTP_PORT: the port number of the SMTP server (must be a StartTLS enabled port!)
* CANARY_SMTP_USERNAME: Username for the SMTP server (no anonymous SMTP supported right now)
* CANARY_SMTP_PASSWORD: the password that corresponds to the username

A complete example config in `switchboard.env` then looks like this:
```
CANARY_SMTP_SERVER=smtp.yourserver.com
CANARY_SMTP_PORT=587
CANARY_SMTP_USERNAME=<your smtp username>
CANARY_SMTP_PASSWORD=<your smtp password>
CANARY_ALERT_EMAIL_FROM_ADDRESS=canary@yourdomain.com
CANARY_ALERT_EMAIL_SUBJECT="Canary Alert via SMTP"
```