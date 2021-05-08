# Cachet Uptime Robot

Cachet is an open source status page system, this repository is a Python script that does two things, **first**, it reads the status of a page in UptimeRobot and updates a cachet component based on that status and **second**, it updates a metric with the historic uptime ratio from Uptime Robot.

### Component status

| Uptime Robot | Cachet |
| --- | --- |
| Not checked yet | Operational |
| Up | Operational |
| Seems down | Partial outage |
| Down | Major outage |

### Getting started 

To get started, you have to specify your Cachet and UptimeRobot settings and in **config.ini**.
```ini
[uptimeRobot] // Global uptimerobot API
UptimeRobotMainApiKey = your-api-key

[cachet] // Global cachet status API
CachetApiKey = cachet-api-key
CachetUrl = https://status.mycompany.com

[uptimeRobotMonitorID1] // This will update ComponentId 1 on the global Cachet
ComponentId = 1

[uptimeRobotMonitorID2] // Still possible to use custom cachet settings 
CachetApiKey = cachet-api-key
CachetUrl = https://status.mycompany.com
MetricId = 1
ComponentId = 1
```

* `UptimeRobotMainApiKey`: UptimeRobot API key.
* `uptimeRobotMonitorID`: This exact "monitor" id set in UptimeRobot. You can find the id's by running `python update_status.py config.ini --printIds`
* `CachetApiKey`:  Cachet API key.
* `CachetUrl`: URL of the API of the status page you want to show the site availability in.
* `MetricId`: (Optional) Id of the Cachet metric with site availability.
* `ComponentId`: (Optional) Id of the component you want to update on each check.

Either `MetricId` or `ComponentId` must be defined per `uptimeRobotMonitorID`

MetricId is special, it will try to sync the graph from UptimeRobot to Cachet. Please keep this in mind at all times.

### Command and args
`update_status.py <config> [--printIds]`  
`config` is mandantory and must point to the path where a config file can be found.  
`--printIds` will print a list with all monitors in UptimeRobot with there name and ID. This ID needed in the config.ini file.

You can always do `update_status.py -h` for more info.

### Usage
Register a cron that runs `update_status.py` every 5 minutes.
```bash
# Open cron file to edit.
crontab -e
```

Edit the crontab file and add this line:
```bash
*/5 * * * * ~/path/run.sh
```

or if you have you're config in a other location:
```bash
*/5 * * * * python ~/path/update_status.py ~/path/config.ini
```

_Note that the path of the update_status.py & config.ini files may vary depending on the location you cloned the repository_

### Running with docker
First, make sure the `config.ini` and the `docker-compose.yml` are in the same directory.
Then run 
```
docker-compose run cachet-uptime
```
if you want to use cron, add the following line into crontab.
```
*/5 * * * * docker-compose -f /path/to/compose/file/docker-compose.yml run cachet-uptime
```

### Running manually

You can also update your Cachet data manually by running this:

```python
python update_status.py

INFO:cachet-uptime-robot:Updating monitor MySite. URL: http://mysite.co. ID: 12345678
INFO:cachet-uptime-robot:HTTP GET URL: https://status.mycompany.com/api/v1/components/1
INFO:cachet-uptime-robot:No status change on component 1. Skipping update.
INFO:cachet-uptime-robot:Updating monitor MySite Mail. URL: http://mail.mysite.co. ID: 12345687
INFO:cachet-uptime-robot:HTTP GET URL: https://status.mycompany.com/api/v1/components/2
INFO:cachet-uptime-robot:Updating component 2 status: 1 -> 4
```
