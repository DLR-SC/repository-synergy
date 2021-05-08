Trillian
========
#### An All-Sky, Multi-wavelength Astronomy Computational Engine

Trillian is an amitious project created and developed by Demitri Muna whose aim is to bridge the gap between astrophysical models and the vast amount of publicly available astronomical data. One of its primary aims is to make the analysis of large volumes of multi-wavelength data as easy as analyzing a single image. It's almost there.

Its principle features include:

* a distributed data scheme
* distributed computation
* integrated API access to disparate data

A more detailed descripton of the project can be found here: [http://trillianverse.org](http://trillianverse.org).

A paper written by Demitri Muna and Eric Huff that describes Trillian in more detail can be found here:  [arXiv:1402.5932](http://arxiv.org/abs/1402.5932).

#### Current Support

Trillian's current development is partially supported by a NASA Astrophysics Data Analysis Program (ADAP) grant. Ongoing hardware support is greatfully acknowledged from the Center for Cosmology and Astroparticle Physics at Ohio State University.



## Where Is The Code?

Trillian has been developed over the past several years and is currently under active development. It is now at an advanced stage of functionality. As a project comprised of many moving parts, it currently consists of:

* a 20+ TB database of metadata, mapping 500+TB of data from a wide range of astronomical data products
* a queing system capable of storing and feeding hundreds of millions units of "work"
* a Python API that provides atomic, random access to the data indexed
* a container-based framework for distributed computation

As the functionality of this project spans these many parts (and more), it is inaccurate to assess the current state of the project from one or a few GitHub repositories. Unfortunately this has happened more than once, so for the time being the code is being removed. I have the full intention to make all of the code open and avaliable (as it should be) at a later date when it is ready to be demonstrated. People are welcome to view code and notes from earlier revisions of this repository, but note that is it is now years out of date and by no means a current reflection of the project.



Links
-----
Project home page: [http://trillianverse.org](http://trillianverse.org)  
Mozilla ScienceLab Collaborate page: [https://mozillascience.org/projects/trillian](https://mozillascience.org/projects/trillian)  
Mailing list: [https://groups.google.com/forum/#!forum/trillianverse](https://groups.google.com/forum/#!forum/trillianverse)  



## What Is Trillian?

Trillian is a project to create a next-generation astronomical archive, allowing astronomers to analyze hundreds of terabytes of data (or more!) as easily as they would dozens of files on their own hard drive.

#### The Problem.

Astronomy has generated *a lot* of freely available, public data. The recent [Pan-STARRS data release](http://panstarrs.stsci.edu) alone is 2PB in size, and that's just one telescope. The data is available through a number of archives around the world such as the [Space Telescope Science Institute](http://archive.stsci.edu),  [IPAC](http://ipac.caltech.edu), or [SDSS](https://dr13.sdss.org). There is no single, central repository of data. These archives are organized by the funding bodies for the telescopes or satellites, e.g. NASA or hosted by the individual surveys. Typically, this means that optical data will be in one archive, radio in another, infrared yet another, etc. This makes sense from an organizational of funding point of view, but it makes life difficult for the individual astronomer.

When an astronomer wants to study a particular set of objects, ideally she wants to get all of the observations that have been made of those objects. First, she must identify the archives that might contain data for those objects. Next, she will go to each of those archives and, most frequently, enter the positions in the sky she wants manually into a web form (where each web form is different) and download the files herself. Extracting the data from the files is another task – while all of the files will likely be in the [FITS format](https://github.com/trillian/trillian/wiki/What-is-a-FITS-file%3F), the data from each telescope or satellite will be organized differently. Finally, she will be able to use her code to analyze the data.

This manual process doesn’t scale to large data sets. The individual astronomer has limited time to visit all of the archives (assuming she is aware of all of them) so she uses the ones she's most familiar with, potentially leaving data on the table. She may be able to download data for hundreds or even thousands of objects, but not millions from several archives. She has limited disk space to download data (so, for that matter, does her department or whole university!). It's impossible to perform an analysis across many different observed wavelengths across the whole sky.

#### The Solution.

Trillian is a framework that aims to solve these problems. First, it is an archive that will organize astronomical data by position on the sky, not by wavelength. Even if you can programatically access all of the data needed remotely, you will spend more of your time waiting to download it.

If we can't bring the data to the astronomer’s code, let's bring the code to the data. By customizing a provided Python module template, the user can write their own, custom module to analzye data. Is radio data available? Let's use it. Are distance measurements available? Use them. The Trillian framework will supply the data available from any data set that has been indexed. The custom code is then placed into a Docker container and send to a server where the data is on disk. The data is analyzed, where the results stored in a database and made available to the user.

This is the only model of data analysis that can currently enable individuals with limited resources to analyze hundreds of terabytes (or even petabytes) of data. It will allow us to ask scientific questions of data – that is currently sitting on disk! – that we lack the tools to ask.



## Mozilla ScienceLab

The [Trillian project](https://science.mozilla.org/projects/trillian) was selected as one of the earliest open source projects of Mozilla Science Lab’s [Collaborate on Software for Science](http://collaborate.mozillascience.org). The recognition of our project and its aims was flattering and very appreciated. The process and inclusion was very instructuve for myself (and, I hope, the Science Lab as well). It provided a great platform to bring people from the general community into a project like this. There were several "lessons learned" for me. First, it's probably best for a project to be at a certain stage of development before people not familiar with the domain (here, handling astrophysical data) can be brought in. A project like this starts with basic architecture — think the foundation of a house. Building this requires deep knowledge of not only the specific problems to be solved but of the eventual usage, each of which require domain knowledge. From my experience and observation, this stage of development is often done by a very small number of people with a shared vision. Once the foundation is laid, it's possible to divide work into small enough units that people without the specific domain knowledge can "swoop in" to help. Another lesson learned is that with open source projects, volunteers can have wildy varying skill sets or backgrounds. Integrating these into a project is possible, but also requires time and attention. This is understandable, but the very nature of volunteered effort means that help can diappear as quickly as it can appear. This is not to challenge the effectiveness of the model, but note only that it is a challenge.

All said, I got a lot out of being a participant of the Mozilla Science Lab and would be happy to continue to support and participate.



## Resources

The Trillian project is being developed at the [Center for Cosmology and Astroparticle Physics](http://ccapp.osu.edu) (CCAPP) at Ohio State University. CCAPP awarded the project a $10K startup fund which was used to purchase a ~30TB server to develop a proof of concept. While certainly not enough for all-sky coverage while trying to include even the most popular data sets, it’s more than enough for a both a proof of concept and scientific inquiry. Two regions on the sky have been chosen initially: SDSS’s Stripe 82 and the Kepler field, selected as they have been heavily studied and are good representative regions for both extragalactic and Galactic science. Data covering as many wavelengths as possible will be collected for these areas.



## Contact

The Trillian project is currently seeking collborators. If you are interested in contributing to this project, please contact [Demitri Muna](http://github.com/demitri).

