dockerpress
===========

Create Docker containers running Wordpress and automatically create a nginx proxy config to map docker port to port 80.


# Nginx as a reverse proxy in front of your Docker containers

I have and create a lot of WordPress sites for clients. As of now, I manually create new Docker container, create a nginx (or [HAProxy](/haproxy-as-a-static-reverse-proxy-for-docker-containers/)) config file so the site can be reached on port 80 from the outside. And it's a pain.

So I created this Python script that takes care of the container and config file creation. All you have to do i to reload nginx and the site will be up.

Check it out: [Script to create wordpress docker container and nginx config file as reverse proxy](https://github.com/oskarhane/dockerpress/blob/master/dockerpress).

This image illustrates what the setup will look like.

![nginx reverse proxy](http://oskarhane.com/wp-content/uploads/2014/03/orreMBA-2014-03-28-kl.-10.59.02.png)

Here's how you use it.

    //Git clone and cd into the dir
    git clone https://github.com/oskarhane/dockerpress.git && cd $_

    //Add execution permission
    chmod +x ./dockerpress

    //Create your first site. The URL MUST match the URL to be used.
    ./dockerpress --url www.yoursite.com

    //If all is ok, reload nginx
    service nginx reload
    //or
    /etc/init.d/nginx reload

If you already pointed the A-record in the DNS to this servers IP, you should be able to see the site. If not, you can reach it via `http://server-ip:http-port`. You find the http-port by typing `docker ps` and read the port (49xxx something) forwarded to 80. It look something like this:

> 0.0.0.0:49222->80/tcp

Wehere 49222 is the port number to enter.

Even though this script specific to one docker image, you can modify it to work with any docker image.
