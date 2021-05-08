# NGECore2

The ProjectSWG Open Source Project's aim is to create a server emulator for the sandbox MMO Star Wars Galaxies at its final publish before
shutdown on 15/12/2011.

The Open Source Version of ProjectSWG is restricted to 30 minutes uptime and upto 5 connections to ensure that the community
is not split between several small servers. This restriction will not be lifted. It is not legal to remove this restriction, per the license.

The Engine (NGEngine) is a closed source library and is only licensed for use with this project. The Core (NGECore2) is licensed under the L-GPL License. By using NGECore2, you agree to the terms of both licenses.

## Requirements for Building the Core:

* JDK 8
* A Java 8 compatible IDE like Eclipse Kepler 
  * https://wiki.eclipse.org/JDT/Eclipse_Java_8_Support_For_Kepler
* A valid Star Wars Galaxies Installation with the final patch
* Postgresql server 
  * http://www.postgresql.org
* PGAdmin (optional, but makes managing the database easier)
  * http://www.pgadmin.org/
* TRE Explorer
  * http://forum.modsource.org/index.php?PHPSESSID=bf02fd8244123807f4716c1686abb59f&action=dlattach;topic=33.0;attach=49
* Github account
* Github for Windows (optional)
  * http://windows.github.com/

### Setting up the core

A video tutorial of this process can be viewed at http://www.projectswg.com/showthread.php?t=40304

1. Once you have met the requirements, fork the project and then proceed to clone your copy of the repository to your computer.
2. Import the project to Eclipse.
3. Create a postgres DB and restore the nge.backup file. Depending on each update, you may or may not have to repeat this process. Once restored, create an account for yourself in the accounts table of your database, and update the connectionServers table with the appropriate IP address of your server, in the address field. 
4. Copy nge.cfg.example to nge.cfg, and add your DB credentials and name.
5. Create a directory named "clientdata" inside your NGECore2 git repo.
5. Open TRE Explorer and proceed open the sku0_client.toc in your SWG directory. Export the following directories to your clientdata directory:

* abstract
* appearance
* creation
* customization
* datatables
* footprint
* interiorlayout
* misc
* object
* quest
* snapshot
* string
* terrain

Repeat the above extraction process with the sku1_client.toc, sku2_client.toc and sku3_client.toc files to avoid errors with kashyyyk.

You are now ready to run the core!

## Contributing and Submitting patches

To contribute, commit your changes to your fork of the project and then submit a pull request. 
 
Your changes will be reviewed by other developers. Once the changes are approved, your pull request will be merged into the main repository.

Please prefix all commits with Added, Changed, Removed or Fixed. If you don't have enough room for multiple changes, use the extended description. Try not to bundle multiple changes into one vague line (ie. "Changed various combat things"). Try to make all commit messages understandable by non-programmers.

* For more information please visit the wiki at https://github.com/ProjectSWGCore/NGECore2/wiki
* Documentation can be found at http://projectswg.com/doc/
