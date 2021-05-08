<h1 align="center">
  <br>
  <a href="http://nameles.org"><img src="https://i.imgur.com/Y7LOWbg.png" alt="Nameles" width="350"></a>
  <br>
</h1>

<h3 align="center">Auditable Invalid Traffic Detection</h3>

<p align="center">

  <a href="https://travis-ci.org/Nameles-Org/Nameles">
    <img src="https://img.shields.io/travis/Nameles-Org/Nameles/master.svg?style=for-the-badge&logo=appveyor" alt="Talos Travis">
  </a>

</p>

<p align="center">
  <a href="#Nameles">Nameles</a> •
  <a href="#Key-Features">Key Features</a> •
  <a href="#Performance">Performance</a> •
  <a href="#Examples">Examples</a> •
  <a href="#Install">Install</a> •
  <a href="#Support">Support</a> •
  <a href="https://nameles.readthedocs.io/en/latest/">Docs</a> •
  <a href="https://github.com/Nameles-Org/Nameles/issues">Issues</a> •
  <a href="#License">License</a> •
  <a href="https://github.com/Nameles-Org/Nameles/archive/master.zip">Download</a>
</p>
<hr>
<p align="center">
Nameles brings state-of-the-art invalid traffic detection, analysis and real-time filtering to every advertiser, data scientist, advertising technology company and trading desk.</p>
<p align="center">
<img src='https://i.imgur.com/AIbUof6.gif' width=550px>
</p>


## Nameles
Nameles provides an easy to deploy, scalable IVT detection and filtering solution that is proven to detect at a high level of accuracy ad fraud and other types of invalid traffic such as web scraping. 

## Key Features

Nameles is an auditable invalid traffic detection, filtering, and analysis platform that can be used by any online advertising stakeholder. Key features include:

- classify websites and apps
- classify traffic sources (IP, device, uuid, etc.)
- pre-bid filtering
- post-campaign data analysis

Nameles is the only detection solution that can be audited by independent parties and that is backed by scientific research and publications. 

Nameles can detect invalid traffic on:

- mobile and desktop 
- display, video, and in-app

Nameles implements a highly scalable entropy measurement using entropy of the IP addresses a given site is receiving traffic from, and then assigns a normalized score to the site based on its traffic pattern.

<img src='https://raw.githubusercontent.com/Nameles-Org/Nameles-logfile/master/CS_formula.png'>

Entropy have been used widely in finance, intelligence, and other fields where dealing with vast amounts of data and many unknowns characterize the problem. The use of Shannon entropy has been covered in hundreds of scientific papers. Some argue that Shannon received it from Alan Turing himself, and that it was the method Turing used for cracking the Nazi code.

## Performance 

Nameles is created to meet the requirements of systems dealing with hundreds of billions of bid requests per day, without introducing any implementation constraints for smaller systems.

Using DSP as an example, a response to a given bid request has to be received by the Ad Exchange within 100 ms. Hence, the delay introduced by Nameles is limited to few ms in order to minimize the impact in the overall bidding process delay. This ensures that also in Exchange use, the strict requirements for avoiding delays on publisher websites are avoided. 

<img src='https://i.imgur.com/HkhDijN.png'>

## Examples

Read an example case where [a DSP implements Nameles](docs/OVERVIEW.md) for real-time pre-bid filtering.

## Getting Started 

    wget https://raw.githubusercontent.com/Nameles-Org/Nameles/master/setup
    chmod +x setup && ./setup
    
More detailed information related with setup options is provided below. 

## Install <a name="install"></a>

You can install Nameless on a single machine or a cluster of multiple machines. Cluster is recommended for pre-bid filtering use.

If you install Nameles on a multiple machine docker cluster/swarm, you have two options: 

- where you let docker allocate resources per service (RECOMMENDED)
- where you allocate resources yourself.

Before starting install:

Read [system setup](docs/SYSTEM.md) and [install](docs/INSTALL.md) related instructions.

## Support

For a high level overview you might want to check out the [website](http://namel.es)

If you have any questions or need support, try the [gitter channel](https://gitter.im/nameles-hub/Lobby)

If you found a bug or have a suggestion for improvements, create [new issue](https://github.com/Nameles-Org/Nameles/issues)

## License

Nameles is available under the permissive [Apache license](LICENSE).