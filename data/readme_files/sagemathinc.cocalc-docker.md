# CoCalc Docker image

[![](https://images.microbadger.com/badges/image/sagemathinc/cocalc.svg)](https://microbadger.com/images/sagemathinc/cocalc "Size and number of layers")

**Run CoCalc for free for a small group on your own server!**

This is a free open-source  multiuser CoCalc server that you can _**very easily**_ install on your own computer or server using Docker.  If you need something to install on a cluster of servers using Kubernetes, see [cocalc-kubernetes](https://github.com/sagemathinc/cocalc-kubernetes).


**LICENSE AND SUPPORT:**
  - Much of this code is licensed [under the AGPL](https://en.wikipedia.org/wiki/Affero_General_Public_License). If you would instead like a business-friendly MIT license instead, please contact [help@cocalc.com](help@cocalc.com), and we will sell you a 1-year license for $799.  This also includes some support, though with no guarantees (that costs more).  We **do** have several happy paying customers as of Sept 2019.
  - Join the [CoCalc Docker mailing list](https://groups.google.com/a/sagemath.com/group/cocalc-docker/subscribe) for news, updates and more.
  - [CoCalc mailing list](https://groups.google.com/forum/?fromgroups#!forum/cocalc) for general community support.

**SECURITY STATUS:**
  - This is _**not blatantly insecure**_ from outside attack: the database has a long random password, user accounts are separate, encrypted SSL communication is used by default, etc.
  - That said, **a determined user with an account can easily access or change files of other users in the same container!** Use this for personal use, behind a firewall, or with an account creation token, so that only other people you trust create accounts.  Don't make one of these publicly available with important data in it and no account creation token! See [issue 2031]( https://github.com/sagemathinc/cocalc/issues/2031).  Basically, use this only with people you trust.
  - See the [open docker-related CoCalc issues](https://github.com/sagemathinc/cocalc/issues?q=is%3Aopen+is%3Aissue+label%3AA-docker).

## Instructions

Install Docker on your computer (e.g., `apt-get install docker.io` on Ubuntu).   Make sure you have at least **15GB disk space free**, then type:

    docker run --name=cocalc -d -v ~/cocalc:/projects -p 443:443 sagemathinc/cocalc

wait a few minutes for the image to pull, decompress and the container to start, then visit https://localhost.  (If you are using Microsoft Windows, instead open https://host.docker.internal/.) It is expected that you'll see a "Your connection is not private" warning, since you haven't set up a security certificate.  Click "Show advanced" and "Proceed to localhost (unsafe)".

NOTES:
 - This Docker image only supports 64-bit Intel.
 - If you get an error about the Docker daemon, instead run `sudo docker ...`.
 - CoCalc will NOT work over insecure port 80.  A previous version of these directions suggested using -p 80:80 above and visiting http://localhost, [which will not work](https://github.com/sagemathinc/cocalc/issues/2000).
 - If you are using Microsoft Windows, instead make a docker volume and use that for storage:
    ```
    docker volume create cocalc-volume
    docker run --name=cocalc -d -v cocalc-volume:/projects -p 443:443 sagemathinc/cocalc
    ```
  - IMPORTANT: If you are deploying CoCalc for use over the web (so not just on localhost), it is probably necessary to obtain a **valid security certificate** instead of using the self-signed unsafe one that is in your Docker container.    See [this discussion](https://groups.google.com/forum/?utm_medium=email&utm_source=footer#!msg/cocalc/7QO1hJQQGYY/Zsev1G72AAAJ).

The above command will first download the image, then start CoCalc, storing your data in the directory `~/cocalc` on your computer. If you want to store your worksheets and edit history elsewhere, change `~/cocalc` to something else.  Once your local CoCalc is running, open your web browser to https://localhost.  (If you are using Microsoft Windows, instead open https://host.docker.internal/.)

The docker container is called `cocalc` and you can refer to the container and use commands like:

```
$ docker stop cocalc
$ docker start cocalc
```

You can watch the logs:

```
$ docker logs cocalc -f
```

However, these logs sometimes don't work.  In that case get a bash shell in the terminal and look at the logs using tail:

```
$ docker exec -it cocalc bash
$ tail -f /var/log/hub.log
```

### OS X -- Clock skew

It is **critical** that the Docker container have the correct time, since CoCalc assumes that the server has the correct time.
On a laptop running Docker under OS X, the clock may get messed up any time you suspend/resume your laptop.  This workaround might work for you: https://github.com/arunvelsriram/docker-time-sync-agent/.

### Chromebook -- yes, it totally works

You can run CoCalc locally on your Chromebook as long as it supports Crostini Linux.


1.  Install (Crostini) Linux support -- search for Linux in settings and enable.
1.  In the Linux terminal, type 
    ```
    sudo su
    
    apt-get update && apt-get upgrade && apt-get install tmux dpkg-dev
    ```
1.  Install Docker [as here](https://docs.docker.com/install/linux/docker-ce/debian/#set-up-the-repository):
    ```
    sudo su

     apt-get install -y \
     apt-transport-https \
     ca-certificates \
     curl \
     gnupg2 \
     software-properties-common &&  \
    curl -fsSL https://download.docker.com/linux/debian/gpg |  apt-key add - && \
     apt-key fingerprint 0EBFCD88  && \
     add-apt-repository \
     "deb [arch=amd64] https://download.docker.com/linux/debian \
     $(lsb_release -cs) \
     stable" && \
     apt-get update  && apt-get install -y docker-ce

    ```
1.  Install cocalc-docker:
    ```
    sudo docker run --name=cocalc -d -v /cocalc:/projects -p 443:443 -p 80:80 sagemathinc/cocalc
    ```
    Type `/sbin/ifconfig eth0|grep inet` in the terminal, and use whatever ip address is listed there -- e.g., for me it was https://100.115.92.198/



### SSH port forwarding

If you're running this docker image on a remote server and want to use ssh port forwarding to connect, type:
```
ssh -L 8080:localhost:443 username@remote_server
```
then open your web browser to https://localhost:8080

For **enhanced security**, make the container only listen on localhost:
```
docker stop cocalc
docker rm cocalc
docker run --name=cocalc -d -v ~/cocalc:/projects -p  127.0.0.1:443:443 sagemathinc/cocalc
```

Then the **only way** to access your CoCalc server is to type the following on your local computer:

    ssh -L 8080:localhost:443 username@remote_server

and open your web browser to https://localhost:8080

### SSH into a project

Instead of doing:
```
docker run --name=cocalc -d -v ~/cocalc:/projects -p 443:443 sagemathinc/cocalc
```

do this:

```
docker run --name=cocalc -d -v ~/cocalc:/projects -p 443:443 -p <your ip address>:2222:22  sagemathinc/cocalc
```

Then you can do:
```
ssh projectid@<your ip address> -p 2222
```

Note that `project_id` is the hex id string for the project *without hyphens*. One way to show project id in this format is to open a .term file in the project and run this command: (This only works in CoCalc in Docker; USER is set differently in production CoCalc.)

```
echo $USER
```

To use SSH key authentication with the Docker container, have your private key file in the usual place in the host computer, for example `~/.ssh/.id_cocalc`, and copy the matching public key into your project's home directory. For example, you could do the following in a .term in your project:
```
cd
mkdir .ssh
chmod 700 .ssh
vi .ssh/authorized_keys
... paste in contents of ~/.ssh/id_cocalc.pub from host computer ...
chmod 600 .ssh/authorized_keys
```


### Make a user an admin

Get a bash shell insider the container, then connect to the database and make a user (me!) an admin as follows:
```
$ docker exec -it cocalc bash
root@931045eda11f:/# make-user-admin wstein@gmail.com
```
Obviously, you should really make the user you created (with its email address) an admin, not me!
Refresh your browser, and then you should see an extra admin panel in the lower right of accounts settings; you can also open any project by directly visiting its URL.

### Reset a user's password

Sign in as a user that is an admin (see the previous section above).  Click on the Admin tab at the top, search for the user, and then click the "Password" toggle, and click "Request Password Reset Link...".

This does NOT set the password.  It just makes a password reset link, which you send your user via some communications channel that works.  You may need this because:

- You do not have email setup.  It is possible to setup Sendgrid so your cocalc-docker image sends out email, but we haven't documented that yet...
- You have email setup, but it sometimes fails for users with aggressive spam filtering.

#### Account Creation Token

After making your main account an admin as above, search for "Account Creation Token" in the Admin tab. Put some random string there and other people will not be able to create accounts in your CoCalc container, without knowing that token.

### Terminal Height

If `docker exec -it cocalc bash` doesn't seem to give you the right terminal height, e.g. content is only displayed in the uppper part of the terminal, this workaround may help when launching bash:

```
docker exec -e COLUMNS="`tput cols`" -e LINES="`tput lines`" -it cocalc bash
```

More information on this issue is in [moby issue 33794](https://github.com/moby/moby/issues/33794).


### Installation for SELinux (Fedora, etc.)

In order to build and run CoCalc on an SELinux box, first set SELinux to permissive:

```
$ setenforce 0
```

<Install cocalc>

Tell docker and SELinux to "play nicely":

```
$ chcon -Rt svirt_sandbox_file_t cocalc
```

return SELinux to enabled:
```
$ setenforce 1
```

-- via [discussion](https://groups.google.com/forum/#!msg/cocalc/nhtbraq1_X4/QTlBy3opBAAJ)


## Your data

If you started the container as above, there will be a directory ~/cocalc on your host computer that contains **all** data and files related to your projects and users -- go ahead and verify that it is there before upgrading. It might look like this:
```
Williams-MacBook-Pro:~ wstein$ ls cocalc
be889c14-dc96-4538-989b-4117ffe84148	postgres    conf
```

The directory `postgres` contains the database files, so all projects, users, file editing history, etc. The directory conf contains some secrets and log files. There will also be one directory (like `be889c14-dc96-4538-989b-4117ffe84148`) for each project that is created.

## Upgrade


To get the newest image, do this (which will take some time):
```
docker pull  sagemathinc/cocalc
```

Once done, you can delete and recreate your CoCalc container: (This will not delete any of your project or user data, which you confirmed above is in ~/cocalc.)

    docker stop cocalc
    docker rm cocalc
    docker run --name=cocalc -d -v ~/cocalc:/projects -p 443:443 sagemathinc/cocalc

Now visit https://localhost to see your upgraded server.

## Adding custom software to your CoCalc instance

The CoCalc Docker images at Docker Hub contain a subset of all the software in at [cocalc.com](https://cocalc.com). At present, the images are about 12 GB while the cloud service has hundreds of GB of packages and libraries.

Suppose you'd like to add software to your local CoCalc instance after installing and starting the Docker container. Here's an example of how to add an install of [texlive-full](https://packages.ubuntu.com/bionic/texlive-full), in case you need more than the minimal `texlive` installation in the published image:

The Docker image is Ubuntu 18.04. You can do

    sudo docker exec -it [container name] bash

to become root in the container, then do

    apt-get install texlive-full

to install the package.

Note that the `texlive-full` package is over 3 GB. So you will need the additional disk space to install it, and it could take several minutes to over an hour to install, depending on your connection to the internet and the speed of your computer.

Additional notes:

* **Be sure to type `umask 022` first** before you install software if you are using a method other than `apt-get`. This step is needed to ensure that permissions are set properly. The default umask is 007. If you use `pip3` or `pip2` without setting the umask to 022, the package gets installed, but it is not *visible* to normal users as a result.
* Most instructions for adding packages to Ubuntu 18.04 should work for CoCalc-Docker, for example `pip install` for Python 2 packages, and `pip3 install` for Python 3 packages.
* Whenever you upgrade your CoCalc image from Docker Hub as described in **Upgrade** above, you will need to repeat the above steps.

## Build

This section is for CoCalc developers.

Build the image:
```
make build-full   # or make build
```

Run the image (to test):

```
make run
```

How I pushed this:
```
docker tag smc:latest sagemathinc/cocalc
docker login --username=sagemathinc
docker push  sagemathinc/cocalc
```

Also to build at a specific commit:
```
docker build --build-arg commit=121b564a6b08942849372b9ffdcdddd7194b3e89 -t smc .
```

## Links

* [CuCalc = CUDA + CoCalc Docker container](https://github.com/ktaletsk/CuCalc)
