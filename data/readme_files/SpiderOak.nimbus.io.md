#Nimbus.io

##What is Nimbus.io 

Nimbus.io is both a commercially available cloud storage service *AND* a free software project others may use and participate in.

The commercial service offers substantial cost savings for archival class data, with initial pricing at $0.06 per GB per month for storage, and $0.06 per GB for outbound bandwidth.

##Background 

Nimbus.io was created to service the backend of our commercial [SpiderOak](https://spideroak.com/) cloud storage, backup, and sync product offered at [SpiderOak.com](https://spideroak.com/).  Nimbus.io is a 4th generation complete rewrite from previous systems, using everything we've learned about storage at scale since 2007.

Nimbus.io is scheduled to be deployed in production use at SpiderOak in 2013, and to fully replace all previous storage systems by the end of 2014.

##Project Status 

The planned commercial Nimbus.io storage service is expected to become available during in 2013.  See the DevelopmentRoadmap.

In *June 2012* the 2nd and 3rd milestones of development were reached, and Nimbus.io is soon entering limited production use at SpiderOak.  

On *15 Feb 2012*, development reached the first major milestone with detailed documentation and functioning implementations of most core components.  It is now usable for development and sustained testing but not recommended for production.   The source code and development infrastructure is now available to others wishing to participate in the effort.

##Free Software 

Nimbus.io server side software is released under the [GNU Affero General Public License version 3](https://www.gnu.org/licenses/agpl.html) (AGPL) and client libraries, benchmark, and testing code are released under the [GNU Lesser General Public License](https://www.gnu.org/licenses/lgpl.html).

The AGPL is the version of the GPL specifically intended for web services.  The terms of the license make the code freely available to others to use and modify with the requirement that if an online service is created using this code, that online service must also be free software.  Note that these requirements ''do not apply'' to those using the Nimbus.io commercial storage service sold and operated by SpiderOak.  Rather, they apply to those who are interested in using the Nimbus.io source code to create their own storage service at their own site.

Nimbus.io joins a relatively small group of commercial [AGPL projects](https://en.wikipedia.org/wiki/List_of_AGPL_web_applications) including [MongoDB](http://www.mongodb.org/display/DOCS/Licensing) and [Gitorious](https://gitorious.org/).

##Official Documentation

The official documentation for Nimbus.io as part of the source code and on the [Nimbus.io website](https://nimbus.io/docs).

Documentation is available in sections:

- [Developer's Guide](https://nimbus.io/docs/developers_guide.html) - For Building Applications Using Nimbus.io for Storage
- [Administrator's Guide](https://nimbus.io/docs/administrators_guide.html) - For running and administering Nimbus.io on your own servers at your own site
- [Internals](https://nimbus.io/docs/internals.html) - For deeper architecture details and documentation needed by developers working on the Nimbus.io system itself.
- [Glossary](https://nimbus.io/docs/glossary.html) - Detailed explanations of terms and concepts used within Nimbus.io.  We recommend interested developers start by reading the glossary straight through.


Documentation is created using [Sphinx](http://sphinx.pocoo.org/) with the HTTP Domain extensions from the contrib package.  Sphinx is also the system used for the official Python docs.

##Purchasing The Commercial Storage Service

The Nimbus.io storage service is scheduled to be commercially available in Q1 2014.  Early access may be provided to developers joining the project and those on the Nimbus.io invitation mailing list.

##Running Nimbus.io Storage Software At Your Own Site

Please read the [Administrator's Guide](https://nimbus.io/docs/administrators_guide.html), particularly the section on "To Cloud or Not to Cloud."

##Joining the Development 

Love storage, distributed, and fault tolerant systems?  You can contribute to Nimbus.io as a free software contributor, and/or we could pay you to work directly with SpiderOak team.

Note that SpiderOak is an all telecommute team of engineers, spread across the US and Europe.  Our internal development process resembles many open source projects.  This makes SpiderOak a great environment for remote work.

##Source Code Access 

All Nimbus related source repositories are available below:

- [Lumberyard](github.com/SpiderOak/lumberyard.git) Python Library for Accessing Nimbus.io
- [ Motoboto](https://github.com/SpiderOak/motoboto.git) Port of the popular "boto" library for accessing S3, ported to use Nimbus.io.  (This is intended to allow projects already using S3 via boto use Nimbus.io with minimal changes.)
- [Motoboto_benchmark](https://github.com/SpiderOak/motoboto_benchmark.git) Benchmarking and stress testing tools for developing Nimbus.io
- [Nimbus.io](https://github.com/SpiderOak/nimbus.io.git) The Nimbus.io storage service itself

##Mailing List, Commit Access, Etc

###Nimbus.io Mailing List

As of 15-Feb-2012, SpiderOak's internal development discussion of Nimbus.io happens on the public mailing list.

We welcome anyone interested in Nimbus.io to join.  This includes developers building storage applications using Nimbus.io or building Nimbus.io client libraries, Administrator's running Nimbus.io at their sites, and especially those working on Nimbus.io storage software itself.  

You can subscribe the the *devel@nimbus.io* mailing list through the [Mailman web interface](https://nimbus.io/dev/mailman/listinfo/devel), or by sending a subscribe request to `devel-request@nimbus.io`.

###Nimbus.io Developer Credentials

 - For developer credentials, send an email to *nimbusiodev@spideroak.com* if you're interested in joining the development effort. We'll arrange source code commit access, etc. for you.
