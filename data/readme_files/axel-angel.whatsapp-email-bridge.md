# OUTDATED

This project is very old and very unlikely to works. At least it would need some adaptation if not major ones. The upstream library changed a lot but maybe the code could be useful in some way so it's kept here as an archive.

# Description
This program allows to make a two-way gateway between your WhatsApp account
and your email address.

This means that this program:
 * (1) Will receive your WhatsApp messages and forward them to your email address
     AND
 * (2) It will forward emails in your IMAP/POP3 (or with SMTP/LMTP) directly to WhatsApp.

# Install
You will need to install yowsup and the dependencies:
```
    pip install yowsup2 python-axolotl parse
```

Then to configure this app, copy and edit the config file in YAML:
```
    cp config.yaml.example config.yaml
    edit whatsapp_config
```

# Configuration (YAML):
In your config.yaml, change fields as necessary:
 * reply: The email address template that's used to reply to WhatsApp messages
  forwarded by email, for example: myaccount+{}@gmail.com . Note that the {} is
  replaced by the destination phone number.
 * whatsapp: Section containing WhatsApp credentials
  * phone: Your phone number using the international format (2 numbers),
      then your local number without the leading zero, eg: 41791234567
  * password: Your WhatsApp password, you should have it already or you
      need to register, read:
          https://github.com/tgalal/yowsup/issues/195#issuecomment-29389646
 * ingoing: Configures where are the messages you write that should be forwarded to WhatsApp. This program will connect through IMAP or POP3 (or can listen as a standalone SMTP server).
  * with: IMAP or POP3 or SMTP or LMTP
  * (look at config.yaml.example for the rest of details)
 * outgoing: Configures where are delivered the received WhatsApp messages to (currently only support: forward by email).
  * with: SMTP # only possible value for now
  * host: SMTP server address
  * port: SMTP server port
  * user: SMTP username to auth (can be empty)
  * pass: SMTP password to auth (can be empty)
  * sendto: Address which receives the WhatsApp messages
  * ssl: 1 or 0 to toggle to connect with SSL
  * force_starttls: 1 or 0 to toggle force STARTSSL at connection time
