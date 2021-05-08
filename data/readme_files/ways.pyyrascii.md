# PyYrASCII

## About

An ASCII version of http://www.yr.no/sted/Norge/Oslo/Oslo/Oslo/time_for_time.html. Created to be run by a finger server.

## Usage

The service can be used in the following ways:

* `finger oslo@graph.no` - norwegian city name
* `finger 0458@graph.no` - norwegian postal code
* `finger newyork@graph.no` - international city name. These are not hourly. Only data for every 6 hours available.
* `o:oslo` to get a one-liner for use in screen, tmux, scripts.
* `finger <city name>+5@graph.no` (forecast from 5 hours ahead in time, max:26)
* `finger <city name>%2@graph.no` (forecast every 2 hours instead of every hour)
* `finger <city name>~100@graph.no` (set screenwidth. default 80. other widths may be ugly)
* `finger @graph.no` - for more information

### Availability

* Finger is supported on all major platforms (Windows, OS X, Linux, FreeBSD, Android, ...). Open up your terminal (or cmd.exe on Windows).
* If you don't have finger available, but have some standard shell tools, try one of the following:
  * `echo oslo|nc graph.no 79`
  * `telnet graph.no 79` (and then type oslo)

## Example

```bash
$ finger oslo@graph.no
                   -= Meteogram for norway/oslo/oslo/oslo =-                    
 'C                                                                   Rain (mm)
 19------                                                             
 17      ------                                                       
 15            ---                                                    
 13               ---                                                 
 11                  ---                                              
  9                                                               ---
  7                     ^^^===                                 ^^^    
  5                           ===---                        ^^^       
  3                             |   ------^^^^^^         ^^^          2 mm
  1                          |  |               ^^^^^^^^^             1 mm
    15 16 17 18 19 20 21 22 23 00 01 02 03 04 05 06 07 08 09 10 11 12 Hour

    SW SW SW  W NW NW NW  W  W  W  W SW SW SW  S  S  S  S  S SW SW SW Wind dir.
     3  2  2  3  3  3  3  2  2  2  2  2  2  2  2  2  3  6  7  6  7  7 Wind(mps)

Legend left axis:   - Sunny   ^ Scattered   = Clouded   =V= Lightning   # Fog
Legend right axis:  | Rain    ! Sleet       * Snow       '  High uncertainty
Weather forecast from yr.no, delivered by the Norwegian Meteorological Institute
and the NRK. Try "finger @graph.no" for more info.
```

For the U.S., thanks to a comment at http://osxdaily.com/2016/02/18/get-weather-command-line-finger-graph/:

```bash
finger oslo@graph.no | sed "s/'C/'F/" | sed 's/^ \?-\?[0-9]\+/{\0{/' | awk -F{ '{if($2 != "") printf "%3i%s\n", $2*1.8+32, $3; else print $1;}'

                   -= Meteogram for norway/oslo/oslo/oslo =-
 'F                                                                   Rain (mm)
 77                                                                   
 73                                                                   
 69                                                               --- 
 66                                                      ^^^=--=--    
 62                                                ^^^^^^             
 59---                                          ^^^                   
 55   =--^^^=--^^^^^^                     =--^^^                      
 51                  ^^^=--=--^^^      =--                            
  9                              =-----                               
  7                                                                   
    20 21 22 23 00 01 02 03 04 05 06_07_08_09_10_11_12_13_14_15_16_17 Hour

    SE SE SE SE SE SE SE SE NW NW NW NW NW SW SW SW SW SW SW SW SW SW Wind dir.
     2  2  1  2  2  2  2  2  0  1  0  1  1  1  2  2  2  1  4  4  4  5 Wind(mps)

Legend left axis:   - Sunny   ^ Scattered   = Clouded   =V= Thunder   # Fog
Legend right axis:  | Rain    ! Sleet       * Snow
```

## Thanks

If you like the service, or want to report bugs, suggestions, etc, please drop
me a line at [finger@falk-petersen.no](mailto:finger@falk-petersen.no).

Thanks to selbekk and karnival for pull requests.

## Requirements for installation (setting up your own service)

* Please checkout https://github.com/ways/pyyrlib to project directory.
* Please checkout https://github.com/ways/pyofflinefilecache to project directory.
* debian packages: `python-mysqldb`

## TODO

* BUG: o: doesn't show full location name
* BUG: Too tall for windows default window size.
* BUG: Temperature sometimes runs of scale in not-hourly mode.
* BUG: Uncertain-rain overwrites the out-of-scale value on top.
* FEATURE: Add arguments to get weather in different format:
  * i:0458 to get an iconic view. ("Fullscreen" or small?)
* IMPROVEMENT: improve 0458%3
* IMPROVEMENT: add text to o: ( "cloudy", "thunder", etc).
* FEATURE: Include warnings (obsforecast). Example:

```xml
<forecast>
<text>
<location name="Oslo">
<time from="2012-06-28" to="2012-06-29" type="obsforecast">
<title>Thursday and Friday</title>
<body>
<strong>Oslo:</strong> Fredag ettermiddag lokalt store nedbørsmengder.
</body>
</time>
<time from="2012-06-29" to="2012-06-30">
<title>Friday and Saturday</title>
<body>
<strong>Østlandet:</strong> Sørøstlig bris, kortvarig liten kuling i Ytre Oslofjord. Noen regnbyger. Fra i ettermiddag sørlig bris, sørvest frisk bris på kysten. Etter hvert skyet eller delvis skyet, stort sett oppholdsvær. I morgen sørlig bris. På kysten sørvest frisk bris som øker til liten kuling utpå dagen. Skiftende skydekke og enkelte regnbyger. Perioder med sol, særlig nær kysten.
</body>
      </time>
    </location>
  </text>
</forecast>
```

* See https://github.com/ways/pyyrlib for TODOs in library.
* FEATURE: allow wind in kmh, mph.
* FEATURE: allow temperature in F.

## Links and mentions

* Source - https://github.com/ways
* Announced - http://www.reddit.com/r/linux/comments/ouday/retro_weather_forecast_finger/
* News article - http://nrkbeta.no/2012/04/06/old-skool-vaervarsling/
* LittlePrinter plugin from Berg Hack-a-day - http://twitpic.com/a298vv http://www.flickr.com/photos/knolleary/7473137758/in/photostream/
* https://hackerb.it/2016/02/15/mit-finger-wetterdaten-abrufen/
* https://twitter.com/ihsandogan/status/699148352940810240?s=03
* http://osxdaily.com/2016/02/18/get-weather-command-line-finger-graph/
* http://localhost.exposed/2016/02/17/command-line-access-to-weather-data/
* http://lifehacker.com/get-a-quick-weather-forecast-with-a-terminal-command-1760639048
* http://ben.hamilton.id.au/how-to/get-the-weather-from-the-command-line
* https://distrowatch.com/weekly.php?issue=20160404
* http://osarena.net/meteorologikes-provlepseis-sto-termatiko-sas

## Similar projects

* https://github.com/fcambus/ansiweather
