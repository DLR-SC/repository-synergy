# Trackography project

The Trackography project is research by [Claudio ࿓  vecna](https://twitter.com/sniffjoke), developed with [Tactical Tech](http://www.tacticaltech.org), as part of the [MyShadow](http://myshadow.org/trackography) project. 

Take a look at the presentation of Trackography at the [31c3](http://media.ccc.de/browse/congress/2014/31c3_-_6299_-_en_-_saal_2_-_201412292200_-_trackography_-_maria_xynou_-_claudio_vecna.html#video) or at its [online slides](http://trackography.github.io/31c3).


*When you access media websites from your country, your Internet connection is being tracked by multiple third parties. And this happens constantly*. That's what we aim to illustrate.

Our aim is to show where our data travels when we visit our favorite news websites through a visualization. We are currently looking for people to collaborate with in various countries in the world which would make this project possible.

# Install

Please, check the file [INSTALL.md](https://github.com/vecna/trackmap/blob/master/INSTALL.md).

## You, your country and the code

This repository contains the software and data source required to detect online trackers.

The collection of data needs to happen in a distributed way, _which means that the software needs to run from each of the selected countries_. This is important because the network and the trackers behave differently based on the specific country of the user.

### Is your country analyzed in Trackography ?

If the answer is **NO** there are two possible reasons:

  * No one has reviewed or created the **media list**, check in [this directory](https://github.com/vecna/trackmap/tree/master/verified_media) and look at the expected format at the bottom of the page. An unverified media list [can be present here](https://github.com/vecna/trackmap/tree/master/unverified_media_list), if not, sent us an email at **trackmap** at **tacticaltech** dot **org** (because we have some not refined list usable as starter) or provide us a list.

  * No one has run the software from your country yet: In this case, read the sections below

If the answer is **YES**: perfect, this means that someone has already run the software. You can still help, because different ISPs and different Geographical locations in a country bring different results. Having multiple results can be useful for further analysis and comparison.

### How can you help ?

**At the moment, we cannot manage new data -the project is temporary in maintenance- mode only :(**

If you're a **Media aware citizen**, we need a reliable media list for every country. What is important is explained above, use git to help us or open an issue.

If you're a **Linux user** you can help run the software and collect results from your country. A distributed effort is required, because the Internet works differently in different locations. You can run the software as explained below, and it will automatically send the results to our server.

# Support the collection

This procedure uses an apt-get based system (Debian/Ubuntu etc). Docker file is available but currently unmaintained.

### Special condition where you can't run the software:

  * over **Tor** network: because a traceroute cannot run over it, this mean that your web connection appear from a different network point that your traceroutes, and this will bring unacceptable results
  * Network filtering ICMP packets: because a traceroute receives ICMP time exceeded packets and the results would be incomplete, this will be display by the software itself
  * **Internet** lines **with a lot of packet loss** (WiFi/WiMax which is far from the access point):  because a traceroute is based on a protocol which does not support re-transmission and the possibility of having incomplete results would be high
  * **VPN** you can run this test via VPN, but you've to specify the country of your endpoint. If you are in the USA and you've a VPN ending in Sweden, you have to specifiy **-c sweden**.


Tor shall be used when the script has completed the collection, because we anonymize the users interacting with us.


## Options

  * **-i**: To be used when you're in an *Instable Internet Connection*, like, a wifi with many packet loss.
  * **-o**: Specify a different output directory: **needed** when are performed multiple tests.
  * **-d**: Disable the data delivery to us. Permit to collect the data and have the file local. (you can send it later with -s)
  * **-X**: loop, perform test, submit result, perform again: forever.

To see a list of countries, just tape *./perform_analysis.py -c something*: the software shows the available countries (or check yourself [here](https://github.com/vecna/trackmap/tree/master/verified_media) )

### Clean the data

When you've completed the collection and the script report:

    Data collected has been sent, Thank You! :)

The collected data are automatically deleted, because if kept, they became a test resumed in the next collection. In order to avoid it, use the option -d (disable send) and then you can send later with -s.

### Risks faced by users under pervasive surveillance

Users in country where Internet control is pervasive, will not raise concern or anomalies.
Censored Internet traffic will appear like a user opening a news agency home page and close after.
Then, a certain amount of "traceroute" traffic, that is a legit and common tool used to check network speed and topology.

If the user has some concern about using Tor, (which is used at the end of the test by us to deliver the test results), can avoid this using the option -d, and later we can figure out a dedicated way to receive the output collected. In this case, please contact the email address with the PGP key specified at the end of this document.

### Step details, timing and resources

Few Bandwidth/CPU/disk resources are needed. It is not possible to make a precise estimation, because the executed operations depend directly on the amount of media websites being analysed. Anyhow, based on the past experience:

  * A list with around 200 media sites starts for (200 + 50) times a "one time browser". It use 5-10 seconds each. More or less spends 300 Kb for each website ( ~75 megabyte used in download ).
  * For every media fetch, 7 to 20 hosts are discovered to be included. The software processes them in the following ways:
    * every host is resolved in an IPv4 address, which helps minimize duplicated results (quite often different hosts have the same IP address). Depends on the first point, but commonly are between 1400 - 1700 unique hosts. This operation requires 10 to 30 minutes.
    * For every resolved IPv4, it performs a reverse DNS resolution. This operation is slower than the previous one and requires at least 30 to 60 minutes.
  * Then, for every unique IPv4 address, start a traceroute. Worst case scenario (and presence of option **-i**) the test will last for two/three hours, but this depends a lot on the number of target hosts.
  * **The software requires more or less 4 hours to be completed and sends to us 8-15 megabytes of data at the end**

**You can interrupt the script execution with control+C**, and when the command is given again, **it will resume the previous execution**. To start a new collection, remove the 'output' directory.

**It is very important to have a stable network**. If you can avoid WI-FI (or be physically near the access point), it would be better.

### The operation performed by the software

  * an HTTP connection (using phantomjs) to every news media under analysis
  * Collects all the third party URLs (trackers, ADS, social), note: all the resource automatically loaded with javascript enable, not the <a href> resources.
  * Dump &lt;object&gt; elements ( Can be used for future analysis. analyzing this code, we can point out [who are the worst tracker ;) ](http://rt.com/usa/175116-white-house-website-canvas-fingerprinting/) this analysis is not yet done.)
  * DNS resolve and reverse of every unique included URL.
  * Performs a traceroute for every included URL
  * GeoIP conversion from every included IP address
  * sends the results to our server (213.108.108.84:32001) or hidden service (mzvbyzovjazwzch6.onion, if you want submit via Tor, use -T)

This shows all the nations capable of knowing which users are visiting the (selected) news media.


# Technopolitical goal

We know that the **online business model is mostly based on tracking**.

If you don't want that a specific company to make money out of your data because you don't like it, or simply don't want be tracked by that company, your only option is to 'opt out'.

But what are the options ? This is one of the first goals of Trackography: to make you aware of the amount of tracking involved when you read the news online of a daily basis. We have addressed the media, because they represent something that involves all active citizens in a country.

But why bother if Google, NewYorkTimes or others track your behavior and interests ? It's pointless to be scared of those organizations. After all, they have done nothing bad against users.

But sadly, the data they collect is extremely valuable for market and political strategies, and such companies have been targeted by intelligence agencies for that precise reason. So it's easier to understand what we want show:
tracking is not something which is only performed by internet companies, but which is also actively used as a nation's asset.

With Trackography we show the invisible links between a news reader from a nation and all the nations that can eventually snoop on their behavior. In a foreign network, you have no rights.

**Is this paranoia ?**

No ;) This has been done by the NSA, which intercepts the advertising network of the Angry Birds game. Angry Birds was the most deployed game, but was still an option for citizens. News media, however, are accessed by the majority of populations around the world and by tracking which websites users access, third parties can gain a unique insight into the types of interests people have, their ideas, beliefs and concerns. In other words, by tracking news media, third parties can map out the interests of individuals and groups and potentially target them. The aim of this project is to expose how the ADS and tracking business works based on third party injections.

And be aware of the nations and companies that can know group[*] behavior, is still good if you consider data as the new profitable treasure.

[*]: Group mean: a nation, a region, a company, an ethnicity, a city, a block in a city, and every other discrimination that can be accomplish by metadata analysis, social network analysis or network analysis.


### Theoretical elements

In this (very first version) of the Trackography project we want answer to the following questions:

  * "Is the online advertising business a potential asset to intelligence agencies ?"
  * "Are users aware of the extent to which their data and browsing habits are exposed on a daily basis?"
  * "Are privacy activists aware of their network path and of its implications ?"
  * "Is online advertising and tracking a good business model for online media ?" (In this case, media is a website which constantly publishes updates on relevant events and their consultancy is therefore not just an option for users, but also a **need** for users).

Due to limited resources from our side, our research might face the following limitations:


  * The GeoIP resolution, from an IP address to a Country, might return a continent (for example, some classes are assigned to Europe, without more precision about the physical location).
  * We're performing traceroute without checking if the resource included is in https/http2 (this happens very seldom, and in these cases we consider the data stored in the recipient country but not exposed in-transit interception and manipulation)
  * Some service providers use Content Delivery Network and this means that in order to interact with them, this might be resolved as part of the same country of the user, also if the content is obviously stored by a foreign country.
  * We cannot know if a service has some Cloud Provider as a backend
  * We cannot automatize the seeking of company information over every tracking agent
  * GeoIP applied to traceroute may return unexpected or doubtful results. A technical progress can be used by interpolating GeoIP + Autonomous System + TLD/domain analysis. GeoIP for sure show: if an IP address is in a country or if an IP address is assigned to a company based on a certain country.

For example:

      traceroute to www.zerocalcare.it (144.76.179.61), 30 hops max, 60 byte packets
       1  172.16.1.1 [*]  6.556 ms
       2  151.6.151.72 [AS1267]  13.176 ms
       3  151.6.92.105 [AS1267]  15.431 ms
       4  151.6.0.80 [AS1267]  16.456 ms
       5  151.6.2.50 [AS1267]  19.675 ms
       6  80.81.192.164 [AS6695]  33.343 ms
       7  213.239.245.6 [AS24940]  42.645 ms
       8  213.239.245.217 [AS24940]  40.540 ms
       9  213.239.245.170 [AS24940]  66.506 ms
      10  213.239.248.196 [AS24940]  49.232 ms
      11  144.76.158.83 [AS24940]  59.938 ms

**11 HOP passing thru None IT IT IT IT DE DE DE DE DE DE**

This is quite easy: the first IP is a private IP address (None), after there are some Italian (my ISP) and then the connection reach a provider in Germany, where the target host is placed. If we take a look hostnames:

      traceroute to www.zerocalcare.it (144.76.179.61), 30 hops max, 60 byte packets
       1  172.16.1.1 (172.16.1.1)  7.504 ms
       2  151.6.151.72 (151.6.151.72)  13.879 ms
       3  151.6.92.105 (151.6.92.105)  20.831 ms
       4  MIOT-RP01-MIOT-T02.wind.it (151.6.0.82)  31.363 ms
       5  MICL-N01-MICA-T02-po02.wind.it (151.6.2.50)  38.390 ms
       6  decix-gw.hetzner.de (80.81.192.164)  36.001 ms
       7  core1.hetzner.de (213.239.245.6)  39.237 ms
       8  core22.hetzner.de (213.239.245.178)  45.404 ms
       9  juniper2.rz20.hetzner.de (213.239.245.158)  46.696 ms
      10  hos-tr6.ex3k3.rz20.hetzner.de (213.239.233.170)  61.476
      11  83.158.76.144-scoundr.el (144.76.158.83)  55.756 ms

Between the hops 5 (from wind.it, my ISP) and 7 (the first gateway of the server I'm contacting) the connection pass through **decix-gw.hetzner.de**, [DE-CIX](http://en.wikipedia.org/wiki/DE-CIX) is a business to business carrier, that is providing a direct connection between the two ISPs. I don't know if the IP 80.81.192.164 of DE-CIX is physically in Italy, in Germany, or in some other place: GeoIP resolve them as "DE" because is assigned to the Germanic company DE-CIX.

In other situation, the [Trackography API](RESTfulAPI.md) return a more unexpected result like:

    {
        "company": "Twitter",
        "country_chain": [
            null,
            "South Africa",
            "South Africa",
            "South Africa",
            "South Africa",
            "South Africa",
            "South Africa",
            "United Kingdom",
            "United States",
            "United States",
            "United States",
            "United States",
            "United Kingdom"
        ],
        "host": "platform.twitter.com",
        "id": "980429ab-5b71-4fd0-8aa7-7eaef4150f84",
        "is_intended_media": false,
        "media_id": "005962d0",
        "media_url": "www.dieburger.com"
    }

This is the GeoIP resolution of a traceroute from the South African ISP **Mweb** to the host platform.twitter.com (hosted by a [CND](http://en.wikipedia.org/wiki/Content_delivery_network) managed by edgecastcdn.net )

It's unexpected, maybe, because can sounds weird from South Africa go in UK, in US and then comeback to UK. but this is due to GeoIP resolution, not to an actual continental travel.
This is an extraction of the traceroute collected:

     8  176.67.177.146 [AS10474] 195.777 ms
     9  4.69.166.129 [AS3356] 176.582 ms
    10  4.69.166.17 [AS3356]  215.669 ms

The hop at position 8 is the last one in South Africa:

    $ host 176.67.177.146
    146.177.67.176.in-addr.arpa domain name pointer be-4-778-thd-p-2.mweb.co.za.

The hop in position 9 is localized as UK, and probably is assigned to an England section of the carrier provider:

    $ host 4.69.166.129
    129.166.69.4.in-addr.arpa domain name pointer vl-3501-ve-115.csw1.London1.Level3.net.

But in fact, [Level3](http://en.wikipedia.org/wiki/Level3) is an USA based carrier, and a CDN role is to be near as possible from the client requesting the content, so is very likely possible that connection never reach USA directly. Still, in Trackography, the connection will be show to reach both UK and USA, because both intelligence agency or lawful enforcement (or unlawful interception) can snitch on this connection.

    $ host 4.69.166.17
    17.166.69.4.in-addr.arpa domain name pointer ae-229-3605.edge4.London1.Level3.net.

Just to be complete, the third hop, position 10, is still resolved as London gateway in Level3 carrier, but is recognized as US by GeoIP.


## SHA 224 checksum of phantomjs

    8a92c174140533998f591d6630fd61577c8d32624d5658655bb7dee8  phantomjs-1.9.8-linux-i686.tar.bz2
    9da120dd1f50e4acc963ca408d6c94db0280b2d16a8b6b1d0d5b4ce4  phantomjs-1.9.8-linux-x86_64.tar.bz2


## Various notes

a brief presentation related on Italian media is here: [Online users tracking: effect, responsibility and countermeasures](http://vecna.github.io)

### Our PGP key

Ok, it mention "TrackMap", is just the unofficial former name of the project. don't mind on that.

    pub   3200R/0x94E7EF47 2014-08-05 [expires: 2015-08-30]
          Key fingerprint = ABC2 7639 5EE3 3245 A0A1  3973 40E2 6C25 94E7 EF47
    uid                    TrackMap project <trackmap@tacticaltech.org>
    sub   3200R/0x504DEBDF 2014-08-05 [expires: 2015-08-30]

You can retrieve this key via keyserver, of using the [git copy of the Projects key](https://raw.githubusercontent.com/vecna/trackmap/master/trackmap_ABC276395EE33245A0A1397340E26C2594E7EF47.asc)


