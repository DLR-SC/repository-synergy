# disq

A [disque](https://github.com/antirez/disque) Python client.

[ ![Build Status](https://travis-ci.org/ryansb/disq.svg)](https://travis-ci.org/ryansb/disq)

Under the hood, this used redis-py's HiRedis implementation and switches out
Redis commands with the disque ones.

## Usage

```
from disq import Disque

c = Disque() # connects to localhost:7711 by default
c.addjob('queuename', 'body') # takes all ADDJOB arguments
# b'DI... job id ...SQ'
c.getjob('queuename')
# [[b'queue', b'DI3971f14a850d9e5b3ca5c881e3dd1ba2a34277b505a0SQ', b'body']]
```

## Status

This library is ready to use with single or multi-node clusters. All commands
are implemented except for `QSTAT` and `SCAN`, which don't exist in the disque
server yet.

## Features

### Connection Balancing

As specified in the [disque README][clients], disq directs read and ack
operations (GETJOB, ACKJOB, FASTACK) to whichever member of the cluster it has
received the most jobs from in the last N seconds.

To change the length of the job count window, use the `job_origin_ttl_secs`
argument when creating the disque client.

## License

This code is released under the ASL2.0, see the `LICENSE` file for details.

## Thanks

Enormous thanks to Salvatore Sanfilippo (antirez) for writing
[disque](https://github.com/antirez/disque) and
[Andy McCurdy](https://github.com/andymccurdy), author of the
[redis-py](https://github.com/andymccurdy/redis-py) module.

[clients]: https://github.com/antirez/disque#client-libraries
