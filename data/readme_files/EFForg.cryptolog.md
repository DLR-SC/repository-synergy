# Cryptolog

Cryptolog is a simple log filter program that reads log file entries from standard input and writes to either a file or pipes them to the standard input of another program (like `logrotate` or `cronolog`). The filter takes the IP address in the entry (everything before the first space character) and encrypts it, throwing away the key.

Technically, cryptolog takes 16 bytes of random data from `/dev/urandom` and stores it in a file (called the salt). It then calculates a sha256 hash of the salt concatonated with the original IP address, base64-encodes that, and chops off the first six characters of the result. That's what gets stored instead of the IP address in the resulting log entry. Of course this means that if someone who wishes to know the original IP addresses gets access to these logs, all they need to know is the salt (which is also stored on the hard drive) to uncover the original IPs. In order to prevent this, the salt gets updated once a day with a new random 16 bytes. At worst, an attacker can only get the last day's worth of original IP addresses.

Cryptolog makes logs that look like this:

    67.169.69.72 - - [12/May/2011:17:58:07 -0700] "GET / HTTP/1.1" 200 430

Look like this instead:

    UkezVh - - [12/May/2011:17:58:07 -0700] "GET / HTTP/1.1" 200 430

The string that replaces the IP address will remain the same for the same day, so you can tell the difference between unique visitors and pageviews.

Here are some example CustomLog lines for your Apache config files:

    CustomLog "| /usr/bin/cryptolog -w /root/cryptolog-access.log" combined
    CustomLog "| /usr/bin/cryptolog -c /usr/bin/cronolog\\\ /root/cryptolog-access-%Y-%m-%d.log" combined
    CustomLog "| /usr/bin/cryptolog -s /tmp/salt_file -w /root/cryptolog-access.log" combined

Notice that if you're using the `-c` option, you need to escape spaces in the command you're running with three backslashes.

## Custom Regex File

You can use the `-r` option to specify a file containing some regex describing the log entry format. The tokens `*IPV6*` and `*IPV4*` can be used as a subsitute for the entire regex of those respective protocols. The group `IP` will be anonymized, so for instance if the file contains the following:

    (?P<IP>*IPV6*)(, )(?P<OTHER>.*)

Then the entry

    ::ffff:8.8.8.8, 10.10.10.10 - - [14/Oct/2015:17:32:51 -0700] "GET /some/url HTTP/1.1" 200 13160

will be anonymized as

    d68qCQ 10.10.10.10 - - [14/Oct/2015:17:32:51 -0700] "GET /some/url HTTP/1.1" 200 13160

## Requirements

 - Python 2.7
 - PyCrypto ~2.6.1

## Setup

### Docker

Just run:

    docker run --rm -it -p 8080:80 hainish/cryptolog
