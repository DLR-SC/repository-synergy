Flake is an HTTP implementation of Twitter's Snowflake written in the Tornado async library. Snowflake is "a network service for generating unique ID numbers at high scale with some simple guarantees." The generated IDs are time plus worker id plus a sequence. Flake will send a 500 response if the system clock goes backwards or if the per millisecond sequence overflows. 

See also, http://github.com/twitter/snowflake.


Usage:
./flake.py --worker_id=WORKER_ID --port=PORT

Where WORKER_ID is a globally unique integer between 0 and 1023. 

The preferred network setup is to have multiple Flake servers and to connect randomly to one of them. Flake responses should be very quick (<10ms) so its reasonable to setup fallover after a short timeout. 


Requirements:

Tornado, http://www.tornadoweb.org/


Example supervisord conf for a two core machine:

[program:flake]
command=/var/www/flake/flake.py --logging=warning --worker_id=%(process_num)d --port=80%(process_num)02d
process_name=%(program_name)s%(process_num)d
numprocs=2
numprocs_start=0 ; be sure to set this offest such that worker_id is unique across all machines in your Flake cluster
autostart=true


Speed:
Flake is reasonably fast. Two Flake processes behind nginx on a 2.4 GHz Core i5 Macbook Pro generate 3500 IDs/sec with a 99th %ile of 11ms (25 concurrent requests).
