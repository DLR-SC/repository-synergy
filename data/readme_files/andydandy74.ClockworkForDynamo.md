[![Current 1.x version](https://img.shields.io/badge/current%201.x%20version-1.34.0-brightgreen.svg)](http://dynamopackages.com/) [![Current 2.x version](https://img.shields.io/badge/current%202.x%20version-2.3.0-brightgreen.svg)](http://dynamopackages.com/) ![Node count](https://img.shields.io/badge/node%20count-437%20%2F%20435-brightgreen.svg)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/andydandy74/ClockworkForDynamo/blob/master/.github/CONTRIBUTING.md) [![Follow me on Twitter for updates](https://img.shields.io/twitter/follow/a_dieckmann.svg?label=Follow&style=social)](https://twitter.com/a_dieckmann) 

![Clockwork logo](clockwork-logo.png)

**Clockwork** is a collection of custom nodes for the [Dynamo](http://www.dynamobim.com) visual programming environment. It contains many Revit-related nodes, but also lots of nodes for various other purposes such as list management, mathematical operations, string operations, geometric operations (mainly bounding boxes, meshes, planes, points, surfaces, UVs and vectors) and paneling. Currently it consists of some 400+ nodes of which a large portion was previously published in a number of separate packages.

## Installation
Installation is simple - just use Dynamo's built-in package manager and search for ```Clockwork```. If you have used some of my previous 0.6.3 packages, please remember to uninstall *all* of them (find a complete list [here](https://github.com/andydandy74/ClockworkForDynamo/wiki/Deprecated-Nodes-&-Packages#pre-clockwork-packages)). Also, always make sure you have the correct version of Clockwork installed that corresponds to your installed version of Dynamo.

## Versions
The different versions are available as separate packages on the package manager. (So far each new major Dynamo version has introduced changes that prevented downward - and sometimes even upward - compatibility of nodes, hence the separate packages...)

Note that Clockwork version numbering follows the Dynamo version the package is currently maintained for, e.g. Clockwork for Dynamo 1.x v**1.0**.XXX is maintained in Dynamo **1.0**.0 while Clockwork for Dynamo 1.x v**1.1**.XXX would be maintained in Dynamo **1.1**.0...
- Clockwork for Dynamo 2.x:<br>[[change log](https://github.com/andydandy74/ClockworkForDynamo/wiki/Version-History#clockwork-for-dynamo-2x)] [[documentation](https://github.com/andydandy74/ClockworkForDynamo/wiki/2.x-Node-Documentation)] [[repository](https://github.com/andydandy74/ClockworkForDynamo/tree/master/nodes/2.x)] [[deprecated nodes](https://github.com/andydandy74/ClockworkForDynamo/wiki/Deprecated-Nodes-&-Packages#clockwork-for-dynamo-2x)] [[samples](https://github.com/andydandy74/ClockworkForDynamo/tree/master/package_samples/2.x)]
- Clockwork for Dynamo 1.x:<br>[[change log](https://github.com/andydandy74/ClockworkForDynamo/wiki/Version-History#clockwork-for-dynamo-1x)] [[documentation](https://github.com/andydandy74/ClockworkForDynamo/wiki/1.x-Node-Documentation)] [[repository](https://github.com/andydandy74/ClockworkForDynamo/tree/master/nodes/1.x)] [[deprecated nodes](https://github.com/andydandy74/ClockworkForDynamo/wiki/Deprecated-Nodes-&-Packages#clockwork-for-dynamo-1x)] [[samples](https://github.com/andydandy74/ClockworkForDynamo/tree/master/package_samples/1.x)]
- Clockwork for Dynamo 0.9.x:<br>[[change log](https://github.com/andydandy74/ClockworkForDynamo/wiki/Version-History#clockwork-for-dynamo-09x)] [[documentation](https://github.com/andydandy74/ClockworkForDynamo/wiki/0.9.x-Node-Documentation)] [[repository](https://github.com/andydandy74/ClockworkForDynamo/tree/master/nodes/0.9.x)] [[deprecated nodes](https://github.com/andydandy74/ClockworkForDynamo/wiki/Deprecated-Nodes-&-Packages#clockwork-for-dynamo-09x)]<br>Last version: 0.90.8 - **not supported any more**
- Clockwork for Dynamo 0.8.2:<br>[[change log](https://github.com/andydandy74/ClockworkForDynamo/wiki/Version-History#clockwork-for-dynamo-082)] [[documentation](https://github.com/andydandy74/ClockworkForDynamo/wiki/0.8.x-Node-Documentation)] [[repository](https://github.com/andydandy74/ClockworkForDynamo/tree/master/nodes/0.8.x)] [[deprecated nodes](https://github.com/andydandy74/ClockworkForDynamo/wiki/Deprecated-Nodes-&-Packages#clockwork-for-dynamo-082)]<br>Last version: 0.82.8 - **not supported any more**
- Clockwork for Dynamo 0.7.x:<br>[[change log](https://github.com/andydandy74/ClockworkForDynamo/wiki/Version-History#clockwork-for-dynamo-07x)] [[documentation](https://github.com/andydandy74/ClockworkForDynamo/wiki/0.7.x-Node-Documentation)] [[repository](https://github.com/andydandy74/ClockworkForDynamo/tree/master/nodes/0.7.x)] [[deprecated nodes](https://github.com/andydandy74/ClockworkForDynamo/wiki/Deprecated-Nodes-&-Packages#clockwork-for-dynamo-07x)] [[samples](https://github.com/andydandy74/ClockworkForDynamo/tree/master/package_samples/0.7.x)]<br>Last version: 0.75.47 - **not supported any more**
- Clockwork for Dynamo 0.6.3:<br>[[change log](https://github.com/andydandy74/ClockworkForDynamo/wiki/Version-History#clockwork-for-dynamo-063)] [[documentation](https://github.com/andydandy74/ClockworkForDynamo/wiki/0.6.3-Node-Documentation)] [[repository](https://github.com/andydandy74/ClockworkForDynamo/tree/master/nodes/0.6.3)] [[deprecated packages](https://github.com/andydandy74/ClockworkForDynamo/wiki/Deprecated-Nodes-&-Packages#pre-clockwork-packages)] [[samples](https://github.com/andydandy74/ClockworkForDynamo/tree/master/package_samples/0.6.3)]<br>Last version: 0.63.3 - **not supported any more**

## Renamed, recategorized and deprecated nodes
During migration from one Dynamo version to the next, I regularly recategorize, relabel and rename a lot of nodes. These changes are documented in an [excel sheet](https://github.com/andydandy74/ClockworkForDynamo/raw/master/NodeList.xls) that contains a list of all nodes within the package.

## Material on this repository
This repository contains the following:
- Directory [maintenance](maintenance) contains scripts that I use to keep Clockwork in shape, e.g. for creating the node documentation on the wiki, extracting Python scripts from custom nodes etc.
- Directory [nodes](nodes) is the actual repository of the custom nodes that I use for versioning nodes in between publishing package updates to Dynamo's package manager - which means you will sometimes find nodes in here that haven't made it onto the package manager yet.
- Directory [package_samples](package_samples) contains simple examples for most of the nodes in Clockwork. I use them for occasional testing, but they should also help explain how to use each node. All samples are available for the current versions - sample support for older versions is patchy at best.
- Directory [workflow_samples](workflow_samples) contains some old sample workflows that I have published online somewhere before. I have also included some of the examples that I used to use for teaching Dynamo as well as some material presented at conferences. Almost all of these are available for Dynamo 0.7.x (as well as 0.6.3). They will not be updated to a current version.

[![Bad Monkeys logo](https://www.badmonkeys.net/wp-content/uploads/2016/12/BadMonkey_finalLogo-01.png)](http://www.badmonkeys.net/)