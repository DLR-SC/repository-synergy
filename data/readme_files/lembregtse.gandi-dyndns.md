--- Notice ---

The development of this tool or myself are in no way involved with Gandi.net.

--- Requirements ---

- Python (>= 2.7)
- Python xmlrpclib 

--- Gandi details ---

API Key (Apply here: https://www.gandi.net/admin/api_key)

--- Usage ---

gandi-dyndns --api=APIKEY --domain=DOMAIN --record=RECORD

--- Readme ---

Currently very lazy but working mode. 
Note that there is a gandi bug, as where the program updates the zone and activates it, gandi does not show this through their webinterface.
I'll be contacting them to fix this.

All communication is done over https.

