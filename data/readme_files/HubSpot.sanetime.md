# sanetime

**A sane date/time python interface:** better epoch time, timezones, and deltas, django support as well

## intro

**sanetime** was written to DRY up all the common date/time manipulations we all do constantly in our code while offering the most simple, versatile, and intuitive client possible.

We've all learned that the only sane way to store times is using epoch time. (You have, haven't you?) 
Unfortunately, manipulating epoch time and timezones with the standard python toolset requires getting up to speed on a menagerie of python modules and concepts: datetime, date, time, calendar, pytz, dateutils, timedelta, time tuples, localize, normalize.

**sanetime** seeks to bring more sanity to the manipulations of epoch time, timezone, time delta, and time generally.

``` python
>>> from sanetime import time,delta   # a tiny taste

>>> time('2012-05-01 22:31',tz='America/New_York').millis
1335925860000

>>> str(time(tz='Europe/London'))   # now in London
'2012-05-29 15:28:05.178741 +Europe/London'

>>> (time(2012,6,1) - time('2012-05-01')).hours
744

>>> (time() + delta(h=12)).s    # epoch seconds 12 hours from now
1338344977
```

## concepts

### time

The `time` class represents a moment in time, internally stored as microseconds since epoch.
A `time` object also has an associated timezone (UTC by default), however the timezone will never be considered during hashing, comparison or equality checks,
i.e.  A moment in `time` experienced in America/New\_York is equal to the same moment in `time` experienced in Europe/Dublin.

### tztime

The `tztime` class is exactly like the `time` object, except that timezone **does** factor into equality, comparison, and hashing.
A moment in `tztime` experienced in America/New\_York is **not** the same as the same `tztime` moment experienced in Europe/Dublin.

### delta

The `delta` class represents a period of time, and provides easy access to all the different ways you might slice and dice this:
micros, millis, seconds, minutes, hours, mean\_days, mean\_weeks, mean\_months, mean\_years.
There are also many different flavors of these: rounded, floored, floated, positional, rounded\_positional.
There is no attempt made in delta yet to be calendar aware (hence the 'mean' prefixes in some cases).

### span

The `span` class represents a window of time ranging from one specific moment in time to another specific moment in time.
You can think of it as a start `time` with a `delta`, or as a start `time` and a stop `time`.

### django

A django model field is also provided: `SaneTimeField`, that makes it super simple to store a sanetime.
They honor the auto\_add and auto\_add\_now features to easily turn your sanetimes into updated\_at or created\_at fields.
And they even work with south out of the box.

## details

### time `from sanetime import time`

#### construction

You can construct a sanetime object from epoch times, datetimes, date/time parts, or from a parseable string.

Epoch microseconds are assumed when no keyword is given.
Intuitive aliases exists for kwargs, be as terse or verbose as you want (us = micros = epoch\_micros = epoch\_microseconds):

``` python
>>> time(1338508800000000)
SaneTime(1338508800000000,<UTC>)

>>> time(micros=1338508800000000)
SaneTime(1338508800000000,<UTC>)

>>> time(millis=1338508800000)
SaneTime(1338508800000000,<UTC>)

>>> time(seconds=1338508800)
SaneTime(1338508800000000,<UTC>)

>>> time(minutes=22308480, tz='America/New_York')
SaneTime(1338508800000000,<DstTzInfo 'America/New_York' EST-1 day, 19:00:00 STD>)
```

If you have the calendar parameters, then construct just as you would a datetime:

``` python
>>> time(2012,1,1)
SaneTime(1325376000000000,<UTC>)

>>> time(2012,1,1,12,30,1)
SaneTime(1325421001000000,<UTC>)

>>> time(2012,1,1,12,30,1,1, tz='America/New_York')
SaneTime(1325421001000001,<DstTzInfo 'America/New_York' EST-1 day, 19:00:00 STD>)
```


If you already have a datetime object, just construct from that:

``` python
>>> dt = datetime(2012,1,1)
>>> time(dt)
SaneTime(1325376000000000,<UTC>)
```


Or construct from a parsable string:

``` python
>>> time('January 1st, 2012 12:30:01pm')
SaneTime(1325421001000000,<UTC>)

>>> time('January 1st, 2012 12:30:01pm', tz='America/New_York')
SaneTime(1325421001000000,<DstTzInfo 'America/New_York' EST-1 day, 19:00:00 STD>)
```


#### arithmetic

Adding any int/long assumes it to be in microseconds.  You can also add any `delta`:

``` python
>>> time(2012,1,1) + 5
SaneTime(1325376000000005,<UTC>)

>>> time(2012,1,1) + delta(hours=5)
SaneTime(1325394000000000,<UTC>)
```


Subtracting two sanetimes produces a `delta`:

``` python
>>> time() - time(2012,1,1)  # time since new year
SaneDelta(15131339063956)

>>> abs(time() - time()).micros  # microseconds to construct a time
30
```


#### conversion

You can easily convert to a timezone-aware datetime or to a "naive" datetime.  They are accessed as properties.

``` python
>>> time(2012,1,1,tz='America/Los_Angeles').datetime
datetime.datetime(2012, 1, 1, 0, 0, tzinfo=<DstTzInfo 'America/Los_Angeles' PST-1 day, 16:00:00 STD>)

>>> time(2012,1,1,tz='America/Los_Angeles').naive_datetime
datetime.datetime(2012, 1, 1, 0, 0)
```

There are other convenience datetime timezone conversions as well.

``` python
>>> time(2012,1,1,tz='America/Los_Angeles').utc_datetime
datetime.datetime(2012, 1, 1, 8, 0, tzinfo=<UTC>)

>>> time(2012,1,1,tz='America/Los_Angeles').utc_naive_datetime
datetime.datetime(2012, 1, 1, 8, 0)

>>> time(2012,1,1,tz='America/Los_Angeles').ny_datetime
datetime.datetime(2012, 1, 1, 3, 0, tzinfo=<DstTzInfo 'America/New_York' EST-1 day, 19:00:00 STD>)

>>> time(2012,1,1,tz='America/Los_Angeles').ny_naive_datetime
datetime.datetime(2012, 1, 1, 3, 0)
```

To epoch times:

``` python
>>> time(2012,1,1).minutes
22089600

>>> time(2012,1,1).seconds
1325376000

>>> time(2012,1,1).millis
1325376000000

>>> time(2012,1,1).micros
1325376000000000
```

long and int conversion just bring back the epoch microseconds

``` python
>>> int(time(2012,1,1))
1325376000000000

>>> long(time(2012,1,1))
1325376000000000L
```


##### date/time parts

You can get at any of the date parts just as you might with datetime properties.  Be careful-- these properties are all singular.  Do not confuse with the plural epoch possiblities of the previous section.  (this ambiguity will be fixed in future versions)

``` python
>>> time().year
2012
>>> time().month
6
>>> time().day
24
>>> time().hour
3
>>> time().minute
42
>>> time().second
12
>>> time().micro
664819
```

### tztime  `from sanetime import tztime`

#### construction

You construct a sanetztime object with all the same possibilities as a sanetime object, but remember, now the timezone matters for equality, comparison, and hashing.
Timezone defaults to UTC if not specified.

``` python
>>> tztime()
SaneTzTime(1358919880245463,<UTC>)  # now

>>> tztime(tz='America/New_York')  # now in New York
SaneTzTime(1358919987623544,<DstTzInfo 'America/New_York' EST-1 day, 19:00:00 STD>)

>>> tztime(ms=1325376000000, tz='America/New_York')  
SaneTzTime(1325376000000000,<DstTzInfo 'America/New_York' EST-1 day, 19:00:00 STD>)

>>> tztime(2012,1,1, tz='America/New_York')
SaneTzTime(1325394000000000,<DstTzInfo 'America/New_York' EST-1 day, 19:00:00 STD>)
```

### delta  `from sanetime import delta`

#### construction

Passing no parameters specifies a 0 delta:

``` python
>>> delta()
SaneDelta(0)
```

a raw arg is assumed to be in microseconds:
``` python
>>> delta(1000)
SaneDelta(1000)
```

there are many keyword possibilities -- be as verbose or terse as you want to be -- but whatever you think it should be likely works:
``` python
>>> delta(hours=30)
SaneDelta(108000000000)

>>> delta(s=30)
SaneDelta(30000000)

>>> delta(seconds=30)
SaneDelta(30000000)

>>> delta(secs=30)
SaneDelta(30000000)
```

weeks and beyond can only be specified as "mean\_" weeks, months, etc.
That is because the specific delta of a specific week could be different depending on when the week falls, and the sanetime library and made no attempt to accomodate this yet.
A "mean\_week" is exactly 7*24 hours.  A "mean_month" is exactly (365*4+1)/4/12*24 hours.  A "mean_year" is exactly(365*4+1)/4*24 hours.

``` python
>>> delta(mean_months=30)
SaneDelta(18144000000000)
```

#### arithmetic

sanedeltas can be added and subtracted from any sanetime or sanetztime as described above.
sanedeltas can also be added and subtracted from one another.
if a raw number is added or subtracted from a delta it is assumed to be in micros.

``` python
>>> delta(h=1) - delta(m=1,s=1)
SaneDelta(3539000000)

>>> delta(ms=1000) - 1000
SaneDelta(999000)
```

#### conversion

delta's can be converted to any epoch number in a number of ways (rounded, whole (i.e. floored), or floated).  When unspecified, they are rounded:

``` python
>>> from sanetime import delta
>>> delta(ms=9482923939).minutes  # rounded
158049
>>> delta(ms=9482923939).rounded_minutes
158049
>>> delta(ms=9482923939).whole_minutes  # floored
158048
>>> delta(ms=9482923939).float_minutes
158048.73231666666
```

you can also slice up deltas into their positional components -- that is, if you wanted to have a delta of 150 seconds show up as 2 minutes and 30 seconds:

``` python
>>> d = delta(s=150)
>>> d.positional_minutes
2
>>> d.positional_seconds
30
```

### span  `from sanetime import span`

#### construction

You can construct from either a start and delta or a start and stop time.  You must provide a kwarg to do the latter.

``` python
>>> span(time(), delta(s=90))
SaneSpan(start=SaneTime(1358925692752574,<UTC>),delta=SaneDelta(90000000))

>>> span(time(),end=time())
SaneSpan(start=SaneTime(1358925841490454,<UTC>),delta=SaneDelta(37))
```

#### methods

``` python
>>> span(time(), delta(s=90)).overlaps(span(time(),end=time()))  # test for overlap
True
```

### django
TODO: write docs (functionality is solid and used without issue in production systems -- just no time for docs yet -- please feel free to help out here)

## other

### docs
Many nice little features are not documented in these pages, and are lying in the code awaiting your discovery.  One day we'll get everything documented...

### faq
Why is everything stored internally as microseconds?

Python's datetime gives us access to microseconds, and since milliseconds would already have us cross the 32bit integer boundary, we might as well capture everything we can and take on microseconds as well.
There are plenty of helpers on the time, tztime, and delta that make using epoch seconds or millis just as easy as using micros.

### design principles
* simple: simplify usecases to single method/property
* intuitive: easy to remember methods/properties, with guessable aliases - be as verbose (and communicative) or as terse (and efficient) as you want to be.  for example  t = time();  t.ms == t.millis == t.milliseconds
* properties whenever sensible: properties are especially useful for django, cuz you can use them directly in templates without having to stage them first in the views.

### links

[sanetime in github](https://github.com/HubSpot/sanetime)  
[sanetime in travis](https://travis-ci.org/HubSpot/sanetime)  
[sanetime in pypi](http://pypi.python.org/pypi/sanetime)  

