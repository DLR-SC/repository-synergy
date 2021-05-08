# AIKIF

#### Artificial Intelligence Knowledge Information Framework (Alpha)

[![Build Status](https://travis-ci.org/acutesoftware/AIKIF.svg?branch=master)](https://travis-ci.org/acutesoftware/AIKIF) [![PyPI version](https://badge.fury.io/py/AIKIF.svg)](http://badge.fury.io/py/AIKIF) [![Code Health](https://landscape.io/github/acutesoftware/AIKIF/master/landscape.svg?style=flat)](https://landscape.io/github/acutesoftware/AIKIF/master) [![Coverage Status](https://coveralls.io/repos/acutesoftware/AIKIF/badge.svg)](https://coveralls.io/r/acutesoftware/AIKIF) [![Requirements Status](https://requires.io/github/acutesoftware/AIKIF/requirements.svg?branch=master)](https://requires.io/github/acutesoftware/AIKIF/requirements/?branch=master)


This is an information classification framework that maps structured or freeform data to
a standard knowledge store.<br />

Manages a dataset of your applications, the source data, parameters, runs and results and then uses your business rules to convert and store the information in a machine usable format.

Your AI software can link to AIKIF by setting up logging watch-points to define success /
failure along with the range of input parameters. Goals and plans are defined by breaking
them down to smaller tasks until the task can be run by a tool in the Toolbox.<br />

A tool is any python wrapped function or application and is easily extensible.<br />



![Overview of AIKIF](https://github.com/acutesoftware/AIKIF/blob/master/doc/AIKIF-Overview.jpg)



## Quick Start
This github repository [https://github.com/acutesoftware/AIKIF](https://github.com/acutesoftware/AIKIF) contains the latest code, but the current public release is available via

`pip install aikif`

To start the API server use `aikif/api_main.py` and run the `tests/test_api.py`

```
 * Running on http://127.0.0.1:5000/
 * Restarting with reloader
127.0.0.1 - - [28/May/2015 19:22:49] "GET /facts HTTP/1.1" 200 -
127.0.0.1 - - [28/May/2015 19:22:49] "GET /help HTTP/1.1" 200 -
127.0.0.1 - - [28/May/2015 19:22:49] "GET /users/1 HTTP/1.1" 200 -
```

 To start the web interface use `aikif/web_app/web_aikif.py` or the batch file `aikif\go_web_aikif`

![screenshot of web interface](https://github.com/acutesoftware/AIKIF/blob/master/doc/web-if-v02.jpg "Screenshot of web interface")


#### Simple Usage
In its simplest form AIKIF can be used to manage your projects and tasks, by updating information from scripts and tracking via the web application
```
my_biz = project.Project(name='Acute Software', type='business', desc='Custom Software')
my_biz.add_detail('website', 'http://www.acutesoftware.com.au')
my_biz.add_detail('email', 'djmurray@acutesoftware.com.au')
```

#### Logging data
You can use AIKIF as a database to manage adhoc data logging tasks
```
proj2 = project.Project(name='Sales Log', desc='Record list of sales')
proj2.add_detail('Note', 'List of sales taken from manual entries in test program')

tbl_exp = cls_datatable.DataTable('expenses.csv', col_names=['date', 'amount', 'details'])
proj2.record(tbl_exp, 'Expense', ['2015-02-13', 49.94, 'restaurant'])
proj2.record(tbl_exp, 'Expense', ['2015-02-15', 29.00, 'petrol'])
proj2.record(tbl_exp, 'Expense', ['2015-02-17', 89.95, 'fringe tickets'])
```

#### Data Collection Usage

```
p = aikif.project.Project('update Country reference', type='Auto')
p.add_task(1, 'download file', aikif.toolbox.web_download)
p.add_task(2, 'extract zip', aikif.toolbox.zip_util)  # not implemented
p.add_task(3, 'overwrite TXT to database staging', aikif.toolbox.data_load)

p.add_param(task=1, url='http://www.')
p.add_param(task=1, dest_zip = 'T:\data\download\country')
p.add_param(task=3, tbl='S_REF_COUNTRY')
p.execute()
```
This will execute the methods for each task using the specified parameters to update the table from the web


#### Map information
Define how columns in raw data should be mapped
```
m = aikif.mapper('custom mapper for countries', tbl = 'S_REF_COUNTRY')
m.add_col('code', data_type='STR', map_to_col='COUNTRY_CODE')
m.add_col('Name', data_type='STR', map_to_col='COUNTRY_NAME')
m.add_col('Continent', data_type='STR', map_to_col='CONTINENT')
m.add_col('Population', data_type='NUMBER', map_to_col='POPULATION')
```


#### Define your own Toolbox methods
Say you have a program 'my_average.py' which calculates averages that you want to include in the toolbox methods
```
t = aikif.toolbox.Toolbox()
t.add_tool(1, 'Calc Average', src=T:\dev\src\python\my_tools\my_average.py')

p2 = aikif.project.Project('Aggregate Country by Continent')
p2.add_task(1, 'Fetch source data', aikif.toolbox.data_view)
p2.add_task(2, 'Aggregate Population', t['Calc Average'])

p2.add_param(task=1, tbl = 'S_REF_COUNTRY' )
p2.add_param(task=2, group_by_col = 'CONTINENT', measure_col='POPULATION' )

p2.execute()  # with no parameters, data outputs to console
```

### More Information
[Requirements Documentation](https://github.com/acutesoftware/AIKIF/blob/master/doc/AIKIF_requirements.rst)<br />
[Design Notes](https://github.com/acutesoftware/AIKIF/blob/master/doc/AIKIF_design.rst)<br />
[Overview Diagram](https://github.com/acutesoftware/AIKIF/blob/master/doc/AIKIF-Overview.jpg)<br />
