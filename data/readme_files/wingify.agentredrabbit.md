# agentredrabbit: Redis to RabbitMQ transport agent

agentredrabbit is a transport agent written in Python which moves data from
Redis to RabbitMQ. It uses multithreaded workers to do the job and supports
failsafe graceful shutdown and recovery.

![agentredrabbit](/docs/flow.png "agentredrabbit")

- `agentredrabbit` on startup loads failed messages from a dump file, if any
- Thread workers synchronize using a global lock when working with failsafe queue
- It polls to check any messages in a Redis list by name `queue:queue1` and pops
  messages in max. chunk size of 100 and tries to publish to RabbitMQ broker
- If message publishing fails, it saves the chunk to an internal failsafe message
  queue (a heap queue), stops consuming from Redis and retries publishing to
  RabbitMQ
- On shutdown, a global event object is used and it dumps any messages from its
  failsafe queue to a dump file
- On connectivity failures, it tries to reconnect to either Redis or RabbitMQ

## Naming conventions and assumptions

- AMQP heartbeat is assumed at 100s.
- AMQP exchange routing key string is of format: hostname.queuename.log
- For every RabbitMQ queue named `q` that is to be transported, the corresponding
  Redis list name is assumed as `queue:q`
- Any service that is populating data in Redis should push in the corresponding
  list(s) using RPUSH, `agentredrabbit` uses LPUSH, LPOP, LTRIM, LRANGE commands
  internally

## Building

Dependencies:

- pika
- redis (with hiredis for fast parsing)
- nose, mock (for tests)
- Local outbound SMTP server for sending email notifications

These are taken care of by the installation procedure.

### Doc generation

To generate documentation of the code:

    $ make docs

This requires `epydoc` and will generate documentation in docs/agentredrabbit.

### Tests

To run unit tests:

    $ make runtests

### Installation

To install agentredrabbit, simply:

    $ make build
    $ make install

## Usage

After installation, get help docs:

    $ agentredrabbit --help

Run with a configuration:

    $ agentredrabbit --config /path/to/conf.cfg

Example of running as a background process manually:

    $ agentredrabbit -c /path/to/cfg > agent.log 2> agent.log &

Using init.d script for process management after `make install`:

    $ /etc/init.d/agentredrabbit {start|stop|restart}

## Author

Rohit "[bhaisaab](http://bhaisaab.org)" Yadav, rohit.yadav@wingify.com

## Contributing

Send a pull request on the GitHub repository: `https://github.com/wingify/agentredrabbit`

You may contact the author and Wingify's engineering team on engineering@wingify.com

## Acknowledgements and Attributions

[Example code of Async publisher using `pika`](https://pika.readthedocs.org/en/latest/examples/asynchronous_publisher_example.html)

## Copyright and License

Licensed under the opensource permissive MIT license.

Copyright 2013 Rohit "[bhaisaab](http://bhaisaab.org)" Yadav, [Wingify](http://engineering.wingify.com/opensource)

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
