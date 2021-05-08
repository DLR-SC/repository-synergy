## PNS

Distributed Push Notification Service for GCM and APNS. Built on REST API. Requires RabbitMQ and PostgreSQL.
Tested on Python v2.7.x

See [Wiki](https://github.com/Turksat/pns/wiki) for what PNS can do for you.

![Architecture Overview](overview.png)

**Generate REST API Documentation**

    git clone git@github.com:Turksat/pns.git
    npm install -g apidoc
    cd pns & apidoc -i ./ -o apidoc/

**Requirements on Debian 7.x**

    echo "deb http://apt.postgresql.org/pub/repos/apt/ wheezy-pgdg main" > /etc/apt/sources.list.d/pgdg.list
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
    
    
    echo "deb http://www.rabbitmq.com/debian/ testing main" > /etc/apt/sources.list.d/rabbitmq.list
    wget --quiet -O - http://www.rabbitmq.com/rabbitmq-signing-key-public.asc | apt-key add -
    
    apt-get update
    
    apt-get install -y python-dev python-pip rabbitmq-server postgresql-9.4 postgresql-server-dev-9.4 \
        libffi-dev supervisor git-core

**Deployment**

Make it sure *PostgresSQL* and *RabbitMQ* services are up and running;

    service postgresql start
    service rabbitmq-server start



Follow steps for deployment (or use Dockerfile [TODO]);

* First of all setup PostgreSQL server and create an user and database. You can get help from [Debian PostgreSQL Documentation](https://wiki.debian.org/PostgreSql).

        postgres=# CREATE USER mypguser WITH PASSWORD 'mypguserpass';
        postgres=# CREATE DATABASE mypgdatabase OWNER mypguser;


* It's recommended to install required python dependency packages by using `virtualenv`.
 
        virtualenv --no-site-packages env
        source env/bin/activate
        pip install -r pns/requirements.txt

* Copy and edit sample `ini` file and set environment variable `PNSCONF` according to path of config file.

        cp pns/config_sample.ini ~/config.ini
        vi ~/config.ini
        export PNSCONF="$HOME/config.ini"

* Create tables

        export PYTHONPATH=$PYTHONPATH:$HOME/pns
        python -c "from pns.models import *; db.create_all()"


*  Now you can test your web service is running

        python pns/pns/run.py
        * Running on http://localhost:5000/

Congrats! You are done. Now we have to daemonize workers and web service application.

* Copy sample supervisor configuration file and edit executables and paths

        cp pns/supervisor_sample.conf /etc/supervisor/conf.d/pns.conf
        service supervisor restart

    Look at [Supervisor Documentation](http://supervisord.org) page for extra configuration options.

* It's recommended to use `nginx ` to proxying requests to gunicorn. `pns/nginx_sample.conf` file includes a basic setup for `proxy_pass`


**APNS Feedback Service**

> The Apple Push Notification service includes a feedback service to give you information about failed remote notifications.
When a remote notification cannot be delivered because the intended app does not exist on the device, the feedback service adds that device’s token to its list.
Remote notifications that expire before being delivered are not considered a failed delivery and don’t impact the feedback service.
By using this information to stop sending remote notifications that will fail to be delivered, you reduce unnecessary message overhead and improve overall system performance.
> [APNS Documentation](https://developer.apple.com/library/ios/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/Chapters/CommunicatingWIthAPS.html)

To start benefit from feedback service you can setup a `cron`. Edit sample configuration file `pns/pns_cron_sample.sh` and copy under preferred `cron` folder (cron.hourly, cron.daily etc.).

    cp pns/pns_cron_sample.sh /etc/cron.daily/pns
    chmod +x /etc/cron.daily/pns


**Running Database Migrations**

Change username and password in `alembic.ini` and run following command in application root directory (be sure `PYTHONPATH` and `PNSCONF` environment variables are set);

    alembic upgrade head
