consul-do
=========

Do something based on leadership status using consul.io

See https://consul.io

Installation
============

It's just a python script with no additional modules. Download it and stick it somewhere.  

*NOTE* A consul agent is required to be installed where you run this script.

Usage
=====

    $ consul-do
    Usage: consul-do KEY [DEBUG]

Useful for running cronjobs in HA mode.

Run something like this on two or more servers:

    *    * * * * /usr/bin/consul-do JOB-1 && /path/to/job1
    */10 * * * * /usr/bin/consul-do JOB-2 && /path/to/job2

Only one of the servers will be elected leader and will therefore run the job. Should the leader fail, a follower will take over.

To enable debug mode, add anything as a second argument. E.g.

    $ consul-do JOB-1 debug
    Running...
    Found nodename: test.internal
    Found KV store
    Found session: e32c055d-c6ed-e277-45ad-079ba218bb01
    Found session node, we're the leader
    ....

If you require a consul ACL

    $ CONSUL_HTTP_TOKEN="mytoken" consul-do ... 


Testing
=======

    $ vagrant up

Run the following on each respective server

    $ consul agent -server -bootstrap-expect 1 -data-dir /tmp/consul -node=agent-one -bind=172.20.20.10
    $ consul agent -server -join 172.20.20.10 -data-dir /tmp/consul -node=agent-two -bind=172.20.20.11
    $ consul agent -server -join 172.20.20.10 -data-dir /tmp/consul -node=agent-three -bind=172.20.20.12

Now you can run a command on each server

    $ while true; do /vagrant/consul-do testing && date; sleep 10; done
