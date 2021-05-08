zabbix-apache-status
====================

Overview
--------
This program gathers data from Apache's built-in status page and 
sends it to Zabbix. The data is sent via the CLI tool zabbix_sender.

*** See http://www.zabbix.com/wiki/templates/apache for a detailed install guide *** 

Author(s)
--------
* Paulson McIntyre (GpMidi) <paul@gpmidi.net>
* Zach Bailey <znbailey@gmail.com>
* Dale Bewley <dale@bewley.net>

Install
=======

Enable Apache server-status
---------------------------
 1. Add this to your Apache config file: 

    ```ApacheConf
    <Location /server-status>
        SetHandler server-status
        Allow from 127.0.0.1
        Order deny,allow
        Deny from all
    </Location>
    ExtendedStatus On # Optional. Must be in global scope and not in a virtual host
    ```
 1. Restart/reload Apache or use ```kill -USR1 `cat /var/run/httpd.pid ```` for zero downtime

Configure Zabbix Server
-----------------------
 1. Import the template file *Template_App_Apache_Status.xml* into Zabbix
 1. Link the *Template_App_Apache_Status* template to the hosts to be monitored

Now continue with either *Zabbix Agent Mode* mode or *Cron* mode.

Zabbix Agent Mode Install
--------------------------
This method relies on your polling interval for an item called *apache.status*, and will honor any maintenance windows.
The check will run on the host being monitored everytime time *apache.status* is polled. This item is defined as a UserParameter like this:

    # returns a single integer, but uses zabbix_sender to populate trapper items
    UserParameter=apache.status,/var/lib/zabbix/bin/check_apache --config /etc/zabbix_agentd.conf

Install on apache server to be monitored and connect to status page on localhost. Assumes zabbix-agent is installed.

 1. Copy bin/check_apache to <some location>, such as */var/lib/zabbix/bin/check_apache*
 1. Run chmod +x on the file
 1. Copy conf/check_apache.conf to your zabbix agent include dir. Probably */etc/zabbix_agentd.conf.d/* 
 - **Tip** Check to make sure your include directory is enabled.
 > grep Include /etc/zabbix_agentd.conf
 1. **Tip** Make sure you have ServerActive and Hostname filled in your config file.
 1. Restart zabbix-agent.

Cron or Remote Mode Install
---------------------------
This method can run remotely or locally via cron. This method relies on your cron scheduler to set the polling interval, and is unaware of any maintenance windows.

Install on Zabbix server or the host to monitor:

 1. Copy bin/check_apache to <some location>, such as /usr/bin/check_apache
 1. Run chmod +x on the file
 1. Add this to crontab to run every minute:
        * * * * * /usr/bin/check_apache --zabbixsource myhostname -z myzabbixserver &> /dev/null
 1. Replace "myhostname" with the hostname (or *name* in the Zabbix GUI)
of the host that the values should be stored with. Replace "myzqbbixserver"
with the hostname/IP of your Zabbix server.

Repeat above cron lines to monitor multiple hosts. Use the -o option if these URL differs from the hostname.

Notes
------
 * Users of cPanel may need to use add the arguments " -l http://localhost/whm-server-status?auto" to prevent a "ValueError: need more than 1 value to unpack". 

License
--------
GPLv2 - See LICENSE file
