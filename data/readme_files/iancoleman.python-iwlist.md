# python-iwlist

Python scanner and parser for wireless networks

## Usage

```
>>> import iwlist
>>> content = iwlist.scan(interface='wlan0')
>>> cells = iwlist.parse(content)
```

## Output

```
>>> print cells

[
    {
        "cellnumber": "01",
        "mac": "00:11:22:33:44:55",
        "essid": "Wireless Network 1",
        "mode": "Master",
        "frequency": "2.437",
        "frequency_units": "GHz",
        "channel": "6",
        "encryption": "off",
        "signal_level": "32",
        "signal_total": "70",
        "db": "-78"
    },
    {
        "cellnumber": "02",
        "mac": "FE:DC:BA:98:76:54",
        "essid": "AB-Guest-Wifi",
        "protocol": "IEEE 802.11bgn",
        "mode": "Master",
        "frequency": "2.462",
        "frequency_units": "GHz",
        "channel": "11",
        "encryption": "wpa",
        "signal_level": "43",
        "signal_total": "100"
    }
]
```

## Notes

Any script calling `iwlist.scan()` should run as superuser to get live values.

## Tests

```
$ python test.py
```
