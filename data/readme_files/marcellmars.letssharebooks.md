[let's share books]
===================

Calibre plugin
======

The easiest way to share your book catalog is to run Calibre's content server (help: http://bit.ly/111IWwt) and let people access your laptop/desktop computer. If you have a server with public URL and know how to set up reverse ssh port forwarding you are probably already doing that. 

Great. 

If not, you should use Calibre plugin:

> https://www.memoryoftheworld.org/blog/cat/tools/


Simple (old way)
======

The easiest way to share your book catalog is to run Calibre's content server (help: http://bit.ly/111IWwt) and let people access your laptop/desktop computer. If you have a server with public URL and know how to set up reverse ssh port forwarding you are probably already doing that. Great. If not, here is the solution if you run GNU/Linux or OSX:

 0. run Calibre's content server (help: http://bit.ly/111IWwt) 
 1. download [letssharebooks.sh] [1] (or on OSX if you want to install it (or even just run it) do your regular: [letssharebooks.dmg][3] 
 
 2. open the terminal and change directory where you downloaded [letssharebooks.sh] [1] 
 3. run it: 

         sh letssharebooks.sh

 4. wait for the output like this:
        
        Check if you started Calibre's content server:
        http://localhost:8080 (help: http://bit.ly111IWwt)
        Hang out at https://chat.memoryoftheworld.org
        Stop sharing books by pressing Ctrl+c
        Your temporary public URL is https://www56581.memoryoftheworld.org

 5. copy your public URL (e.g. https://www56581.memoryoftheworld.org) and share it with your friends

If you run Windows:

 0. run Calibre's content server (help: http://bit.ly/111IWwt) 
 1. download [letssharebooks_windows.zip] [2]
 2. get to the directory where you uncommpressed .zip file
 3. double-click on letssharebooks file (or letssharebooks.bat if it shows file extension)
 4. it will open a window and you should wait for the output like this:
        
        Check if you started Calibre's content server:
        http://localhost:8080 (help: http://bit.ly111IWwt)
        Hang out at https://chat.memoryoftheworld.org
        Stop sharing books by pressing Ctrl+c
        Your temporary public URL is https://www56581.memoryoftheworld.org

 5. copy your public URL (e.g. https://www56581.memoryoftheworld.org) and share it with your friends


Explanation
===========

Here is the code of this simple shell script:

        #! /bin/sh

        echo " Check if you started Calibre's content server:"
        echo " http://localhost:8080 (help: http://bit.ly111IWwt)"
        echo " Hang out at https://chat.memoryoftheworld.org"
        echo " Stop sharing books by pressing Ctrl+c"

        exec 3>&1
        ssh -N -T -o StrictHostKeyChecking=no -o UserKnownHostsFile=.userknownhostsfile -o TCPKeepAlive=yes -o ServerAliveINterval=60 ssh.memoryoftheworld.org -l tunnel -R 0:localhost:8080 -p 722 2>&1 1>&3 | sed 's|^Allocated port \([[:digit:]]\{4,5\}\)\(.*\)| Your temporary public URL is https://www\1.memoryoftheworld.org|'
        
The "echo" lines are just reminding about starting Calibre's content server (by default port 8080), how to check if it works locally (http://localhost:8080), where to hang out with other librarians and book lovers and how to shutdown the script.

The "ssh" line makes reverse ssh tunnel with dynamic port allocation from the server. The "sed" part only parse the output from server and makes the public URL to be copied and shared.

The whole script has hardcoded domain, ssh user, and ports. It should work for all the newbies. It is super easy to change few things for anyone running calibre-server on non-default port (8080) or running it's own public server.

*Yes, this can be used for free riding with "-D 1234" but until it is misused this server will be left this simple. It's about the trust, right? :)*

If you want to start calibre-server without opening GUI I recommend:

        calibre-server --max-cover=300x400 -p 8080
        
or daemonized:

        calibre-server --daemonize --max-cover=300x400 -p 8080

If you run default set up on Mac OSX you should replace calibre-server with:

        /Applications/calibre.app/Contents/MacOS/calibre-server
        
or on Windows:

       C:\Program Files\calibre2\calibre-server.exe       

Server setup
============

Requirements
============

 * a server with a public ip (e.g. 1.2.3.4)
 * a domain name (e.g. memoryoftheworld.org)
 * a wildcard dns entry in the domain pointing to the public ip 
  (e.g. *.memoryoftheworld.org.    1800    IN  A   1.2.3.4)
 * nginx
 * sshd

Nginx config
============

A wildcard dns should point to this nginx instance.
Every `www<port>.memoryoftheworld.org` will be proxied to `127.0.0.1:<port>`

Where `<port>` needs to be 4 or 5 digits.


        server {
          server_name   "~^www(?<port>\d{4,5})\.memoryoftheworld.org\.org$";

	  listen 80;
	  listen 443 default ssl;
	  ssl_certificate /path/to/cert;
	  ssl_certificate_key /path/to/cert_key;

          location / {
		proxy_pass        http://127.0.0.1:$port;
		proxy_set_header  X-Real-IP  $remote_addr;
		proxy_set_header  Host $host;
		proxy_redirect http:// https://;
		}
        }



SSH configuration
=================

A sshd configuration to allow a user with no password and a forced command, so that the user can't get shell access.

        Match User tunnel
         # ChrootDirectory
         ForceCommand /bin/echo do-not-send-commands
         AllowTcpForwarding yes
         PasswordAuthentication yes
         PermitEmptyPasswords yes

PAM needs to be disabled if sshd is to allow login without a password. That's not always possible, is not even smart. Another approach would be a separate instance of sshd, on a different port, just for the tunnel user (and that's how it is set up at memoryoftheworld.org at the moment)

Make a copy of the config file, change/add these settings:

        UsePAM no
        AllowUsers tunnel
        Port 722

And then run `sshd -f /etc/ssh/sshd_config_tunnel`.

The `tunnel` user has an empty password field in /etc/shaddow.

        tunnel::15726:0:99999:7:::

Credits
=======

There was a version of [let's share books] made by Marcell Mars with ssh autorhization and then jabber client/server conversation + mumbojumbo sysadmin magic in order to provide ssh tunneling. It worked. But...

Damjan Georgievski (https://github.com/gdamjan), kung fu master, made it dead simple: https://gist.github.com/gdamjan/4586758. Now I just build from there.

[1]: https://raw.github.com/marcellmars/letssharebooks/master/letssharebooks.sh    "letssharebooks.sh"
[2]: https://github.com/marcellmars/letssharebooks/raw/master/windows/letssharebooks_windows.zip "letssharebooks_windows.zip"
[3]:https://raw.github.com/marcellmars/letssharebooks/master/osx/letssharebooks.dmg "letssharebooks.dmg"
