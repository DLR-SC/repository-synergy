Generates 'people who read this also read...'-style recommendations based on the [Jaccard similarity](http://en.wikipedia.org/wiki/Jaccard_index) between their readership sets. This code scales to large (1B rows) datasets in limited memory by using external sorting and [locality sensitive hashing](http://en.wikipedia.org/wiki/Locality_sensitive_hashing). Built for [Springer](http://link.springer.com).

# Installation (on Ubuntu 11.04)

Install dependencies

``` bash
sudo apt-get install build-essential python python-dev python-pip ipython git-core
sudo pip install ujson
```

Setup springer-recommendations

``` bash
git clone git://github.com/jamii/springer-recommendations.git
sudo mkdir -p /mnt/var/springer-recommendations
sudo chown $USER:$USER /mnt/var/springer-recommendations
```

# Operation

The recommendations engine reads a newline-separated list of input filenames on stdin and prints a list of recommendations on stdout.

Each input file should contain a newline-separated list of json-encoded [user, doi] pairs. The user field may be any unique string eg ip address or session id.

``` json
["1yud2mlgpalm2cqeyyz0o44n","10.1007\/s10526-004-6592-1"]
["q4lprrkmbr3gpvosjao0dzwm","10.1007\/978-3-540-69934-7_13"]
["3jc2hnohgreyhvlurpg3m1sn","10.1007\/978-3-8348-8229-5_14"]
["uigkldnerjvgghxvjp2ptm0i","10.1007\/s00125-009-1355-2"]
["mmnqkjwawkcz4tqjcxfam4jz","10.1007\/978-3-8274-2313-9_4"]
["e3ie31mmad2epuxno1gpidmx","10.1007\/s10549-012-2108-3"]
["1adokad3mbbg0aaexcl1yb3a","10.1007\/978-3-8349-6622-3_5"]
["fzfrjqgnizgprfxstcal12fu","10.1007\/978-3-7643-8777-8_1"]
["ihcnriijo040rchrgbytvlpg","10.1007\/BF00309663"]
```

For each DOI in the logs, the output contains a line of related DOIs and their Jaccard similarity to the first DOI.

``` json
["10.2478\/s11532-009-0129-5",[["10.1007\/978-1-61737-985-7_11",0.24],["10.1007\/BF01011432",0.56],["10.1007\/BF01524716",0.11],["10.1007\/BF02458601",0.87],["10.1007\/s002140050205",0.97]]]
["10.2478\/s11532-010-0087-y",[["10.1007\/BF02660070",1.0],["10.1007\/BF02988680",1.0],["10.1007\/s00709-010-0225-6",1.0],["10.1007\/s00709-010-0233-6",1.0],["10.1023\/A:1022137619834",1.0]]]
["10.2478\/s11534-010-0072-2",[["10.2478\/s11534-011-0014-7",1.0]]]
["10.2478\/s11534-011-0014-7",[["10.2478\/s11534-010-0072-2",1.0]]]
["10.2478\/s11535-011-0006-z",[["10.1007\/BF02532915",1.0],["10.1023\/A:1013623806248",1.0],["10.1134\/S1019331608020019",1.0]]]
```

Example usage:

``` bash
find /mnt/var/springer-recommendations/logs-*.json | nohup python springer-recommendations/src/recommendations.py > recommendations.json 2> recommendations.log &
```
