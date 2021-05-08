Twisted MySQL Protocol implementation v0.4

With thanks to _habnabit for the intial code (which did the vast majority of
the heavy lifting) and his qbuf library, and Dev0n for DATETIME and
affected_rows support on the result of a runOperation.

PREREQUISITES:

    * qbuf (a Python C-extension)

FEATURES:
    * Connects lazily to MySQL and disconnects if the connection is left
      idle longer than idle_timeout
    * Reconnects on errors when there are pending queries (including
      user-configurable errors with temporary_error_strings=[...] in the
      constructor)
    * Now has unit tests
    * Support escaping arguments with '%s' style syntax
    * Actually use the database=foo argument passed into the constructor
      (need to set CLIENT_* flag)
    * Code comments, and a lot of tidying up
    * Fixed insidious bug relating to disconnection which resulted
      in corrupt/duplicated results getting sent on the wrong deferreds
    * MySQL DATETIME fields now show up correctly (XXXX-XX-XX XX:XX:XX).
    * When a runOperation is called, the deferred now returns the a dictionary
      with the following:
        - {'insert_id': int, 'affected_rows': int, 'message': str,
           'warning_count': int, 'server_status': int}

TODO:

    * Transaction support
    * Stored queries
    * Connection pool
    * DBAPI support - see http://www.python.org/dev/peps/pep-0249/
    * Test against more than just the version of MySQL 5.1 which happened
      to be installed on my ThinkPad :-)


EXAMPLE USAGE:

import sys

from twisted.internet import reactor, defer
from twisted.python import log

from txmysql import client

log.startLogging(sys.stdout)

def example():
    conn = client.MySQLConnection('127.0.0.1', 'root', secrets.MYSQL_ROOT_PASS,
            idle_timeout=120, connect_timeout=30)
    # This gets remembered and re-run if the connection needs reconnection
    d = conn.selectDb("foo")
    def selectedDb(ignored):
        return conn.runOperation("insert into bar set baz='bash'")
    d.addCallback(selectedDb)
    def doneInsert(ignored):
        return conn.runQuery("select * from bar")
    d.addCallback(doneInsert)
    def gotResult(data):
        print repr(data)
    d.addCallback(gotResult)
    def handleFailure(reason):
        # reason can be a MySQLError with message, errno, sqlstate, query
        print reason
    d.addErrback(handleFailure)
    return d

if __name__ == "__main__":
    reactor.callWhenRunning(example)
    reactor.run()


SHAMELESS PLUG: 

txMySQL is used in production by Hybrid Web Cluster, which is an n-redundant
web cluster with no single point of failure, which uses ZFS replication to
eliminate shared storage in loosely coupled, geographically distributed web
hosting environments. Entire data centres can fail and everything carries on
running, with data loss and downtime measured in seconds, not hours or days,
and stress caused by hardware or network connectivity failures a thing of the
past.

It runs on dedicated hardware and/or cloud infrastructure, enabling hybrid
setups where you use dedicated hardware for performance and cloud
infrastructure for ease-of-provisioning, all within the same cluster.

Check it out at http://www.hybrid-cluster.com/.  If you are involved with
hosting websites or know anyone who is, please spread the word :-)

If you just want web hosting for your own site, we offer rock solid hosting
based on the aforementioned technology at http://www.hybrid-sites.com/.

QUESTIONS?

Email luke [at] hybrid-logic [dot] co [dot] uk

