# what & why?

Measuring Co2 and Temperature at [Woogas office](http://www.wooga.com/jobs/office-tour/).

People are sensitive to high levels of Co2 or uncomfortably hot work environments, so we want to
have some numbers. It turns out that our [office](https://metrics.librato.com/share/dashboards/l7pd2aia) does
vary in temperature and Co2 across the floors.

# requirements

## hardware

1) [TFA-Dostmann AirControl Mini CO2 Messgerät](http://www.amazon.de/dp/B00TH3OW4Q) -- 80 euro

2) [Raspberry PI 2 Model B](http://www.amazon.de/dp/B00T2U7R7I) -- 40 euro

3) case, 5v power supply, microSD card

## software

1) [Librato](https://www.librato.com) account for posting the data to.

2) download [Raspbian](https://www.raspberrypi.org/downloads/) and [install it on the microSD](https://www.raspberrypi.org/documentation/installation/installing-images/README.md). We used [this version](https://github.com/wooga/office_weather/blob/0da94b4255494ecbcf993ec592988503c6c72629/.gitignore#L2) of raspbian.

# installation on the raspberry

0) Boot the raspberry with the raspbian. You'll need a USB-keyboard, monitor and ethernet for this initial boot. After overcoming the initial configuration screen, you can login into the box using ssh.

1) install python libs
```
sudo apt-get install python-pip python-dev libyaml-dev
sudo pip install librato-metrics
sudo pip install pyyaml
sudo pip install requests
```

2) create `config.yaml` with [libratro](https://www.librato.com) credentials:
```
user: your.librato.user.name@some.email.com
token: abc123...
prefix: office.floor3
```

We use [librato](https://www.librato.com) to graph our weather, so you'll need to modify that if you using another service.

2b) (optional) You can configure this bot to automatically post to a Slack channel.
Just add an "Incoming Webhook" to your Slack team's integrations and add a `slack` hash to the config file.

```yaml
slack:
    webhook: 'https://hooks.slack.com/services/TXXXXXX/XXXXXX/xxxxxxx'
    channel: '#general'   # optional - this is the default value
    botname: 'CO2bot'     # optional - this is the default value
    icon: ':monkey_face:' # optional - this is the default value
    upper_threshold: 800  # optional - this is the default value
    lower_threshold: 600  # optional - this is the default value
```

3) fix socket permissions
```
sudo chmod a+rw /dev/hidraw0
```

4) run the script
```
./monitor.py /dev/hidraw0
```

5) run on startup

To get everything working on startup, need to add 2 crontabs, one for root
and the other for the pi user:

Roots:

```
SHELL=/bin/bash
* * * * * if [ $(find /dev/hidraw0 -perm a=rw | wc -l) -eq 0 ] ; then chmod a+rw /dev/hidraw0 ; fi
```

Pi:

```
SHELL=/bin/bash
* * * * * /usr/bin/python /home/pi/monitor.py /dev/hidraw0 [ **optional:** /home/pi/my_config.yaml ]  > /dev/null 2>&1
```

The script will default to using "config.yaml" (residing in the same directory as the
monitor.py script - /home/pi in the example) for the librato credentials.
You can optionally override this by passing a custom configuration file path as a second parameter.

# ansible deployment on the raspberry

For this deployment process you need a machine with a working version of ansible.

0) Install raspbian on all deployment targets aka raspberries. Collect their IP addresses either manually using a screen and a keyboard or through the log of your router.

1) In the project folder create the `config.yaml` file as described in the chapter for the manual installation process. Replace the line containing the `prefix` assignment by:

`prefix: {{ name }}`

2) In the project folder create a file called `inventory` and insert the previously collected IP addresses with the respective future librato metric names of the raspberries, e.g.:

```
    192.168.2.12 name=office.floor4.kitchen
    192.168.2.13 name=office.floor4.entrance
```

3) After all preparations are done, the real deployment step may be started by executing:

`ansible-playbook -k -i inventory office_weather_ansible.yaml --extra-vars "new_password=your_new_password"`

Right after starting the command ansible will ask you for the SSH password to access the raspberries.

*The ansible script expects that you provide a new password, which will be set on all raspberries.*


# credits

based on code by [henryk ploetz](https://hackaday.io/project/5301-reverse-engineering-a-low-cost-usb-co-monitor/log/17909-all-your-base-are-belong-to-us)

# license

[MIT](http://opensource.org/licenses/MIT)
