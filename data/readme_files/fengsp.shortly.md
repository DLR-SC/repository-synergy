shortly
=======

A URL shortener

![shortly](http://img5.douban.com/view/photo/photo/public/p2178348756.jpg)

##install

    $ git clone git@github.com:fengsp/shortly.git
    $ cd shortly
    $ pip install -r requirement.txt
    # maybe you need to configure redis (default localhost:6379 db:0)
    $ view shortly/settings.py
    
##usage
For a try out:
    
    $ python fire.py

Shortly should be up on http://127.0.0.1:5000/, type any url to shorten it. We assume you get **abc** back, just go to http://127.0.0.1:5000/abc for a redirect.

<br/>
For a deployment(root privilege is needed):
    
    $ supervisord -c supervisord.conf