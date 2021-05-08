Pinrepo
=======

Pinrepo is a highly scalable solution for storing and serving build artifacts such as debian
packages, maven jars and pypi packages.

* **Simple**: publish and store build artifacts in AWS S3; serve with Nginx reverse proxy
* **Extensible**: could easily add other format support such as RPM
* **Reliable**: highly available nginx cluster and AWS S3 service
* **Scalable**: nginx layer scales horizontally; AWS S3 backend is highly scalable
* **Devops-friendly**: has been running in production for 8 month with virtually no maintenance

Find more details on the design at http://engineering.pinterest.com/.

1. [nginx](nginx/) contains a Makefile to build a simple nginx with the minimum set of modules
to run Pinrepo.

2. [deb](deb/) contains an nginx config file for debian package repo and instructions to publish
debian packages

3. [maven](maven/) contains an nginx config file for maven repo and instructions to publish
maven jars

4. [pypi](pypi/) contains an nginx config file for pypi repo, the pypi-release source code and
instructions to publish pypi packages

### A note about S3 region
The list of available regions can be found under [http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region](http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region)

If you use the US Standard default region, specify `external-1` as the region variable.

