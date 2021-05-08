# Example usage
You can register a whatsapp client with the [yowsup-cli](https://github.com/tgalal/yowsup/wiki/yowsup-cli-2.0#yowsup-cli-registration)

```python
from whatsapp import Client

phone_to = '31641371199'

client = Client(login='3161516888', password='secretpasswordbase64')
client.send_message(phone_to, 'Hello Lola')
client.send_media(phone_to, path='/Users/tax/Desktop/logo.jpg')
```

# Installation
```
$ pip install pywhatsapp
```