For support questions, please send them to the following support mailing list:

- ngs-amsupport@thermofisher.com (Americas)
- ngs-eusupport@thermofisher.com (EMEA)
- ngs-gcsupport@thermofisher.com (Greater China)
- ngs-sasiasupport@thermofisher.com (South Asia)
- jptech@thermofisher.com (Japan)

APAC customers, please contact your local sales representative, Field Service Engineer or Field Bioinformatics Specialist


Please see buildTools/BUILD.txt for build requirements and instructions.
Note especially the section BUILD SPECIFIC MODULES.

To build Analysis module, the command is:

    MODULES=Analysis ./buildTools/build.sh


Tips:

- If you are building this software for the first time, it's suggested to use
  a Docker container to build. That will reduce the chance of being blocked by
  any environment dependencies.

  https://hub.docker.com/r/iontorrent/tsbuild/

- Note that the code that was formerly in the ion-alignment and tmap packages is now
  rolled into the ion-analysis packages

- For standalone Torrent Variant Caller, please see the below link for instructions.
  There are supported Docker containers for various platform.

  http://updates.iontorrent.com/tvc_standalone/README.txt
  https://hub.docker.com/r/iontorrent/tvcbuild/

