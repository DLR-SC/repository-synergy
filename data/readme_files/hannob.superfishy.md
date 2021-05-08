superfishy
==========

Archive of software, links and other data involved in the Superfish / Komodia incident

warning and password
====================

You don't want to install any of the software here if you are not doing this
for security research. All provided downloads contain dangerous software, if
you use them you will endanger the security of your system. To make sure
nobody accidently installs it they are packed in password-protected zip
files. The password for all files is

 iknowwhatimdoing

background / links
==================

Test if you are affected:

* https://superfish.tlsfun.de/ (my own, individually checks all known certs)
* https://filippo.io/Badfish/
* https://www.canibesuperphished.com/

Some of my blog posts:

* [Software Privdog worse than Superfish](https://blog.hboeck.de/archives/865-Software-Privdog-worse-than-Superfish.html)
* [PrivDog wants to protect your privacy - by sending data home in clear text](https://blog.hboeck.de/archives/866-PrivDog-wants-to-protect-your-privacy-by-sending-data-home-in-clear-text.html)
* [How Kaspersky makes you vulnerable to the FREAK attack and other ways Antivirus software lowers your HTTPS security](https://blog.hboeck.de/archives/869-How-Kaspersky-makes-you-vulnerable-to-the-FREAK-attack-and-other-ways-Antivirus-software-lowers-your-HTTPS-security.html)
* [More TLS Man-in-the-Middle failures - Adguard, Privdog again and ProtocolFilters.dll](https://blog.hboeck.de/archives/874-More-TLS-Man-in-the-Middle-failures-Adguard,-Privdog-again-and-ProtocolFilters.dll.html)

My own news coverage in German media:

* [Golem.de / Adware: Lenovo-Laptops durch Superfish-Adware angreifbar](http://www.golem.de/news/adware-lenovo-laptops-durch-superfish-adware-angreifbar-1502-112460.html)
* [Golem.de / Komodia-Filter: Superfish-Affäre weitet sich aus](http://www.golem.de/news/komodia-filter-superfish-affaere-weitet-sich-aus-1502-112502.html)
* [Zeit Online / Superfish: Lenovo steckt gefährliche Adware in seine Laptops](http://www.zeit.de/digital/datenschutz/2015-02/superfish-lenovo-adware-hebelt-https-aus)
* [Golem.de / Privdog: Software hebelt HTTPS-Sicherheit aus](http://www.golem.de/news/privdog-software-hebelt-https-sicherheit-aus-1502-112534.html)

Some english news articles:

* [Arstechnica / Lenovo PCs ship with man-in-the-middle adware that breaks HTTPS connections ](http://arstechnica.com/security/2015/02/lenovo-pcs-ship-with-man-in-the-middle-adware-that-breaks-https-connections/)
* [Wired / Lenovo’s Response to Its Dangerous Adware Is Astonishingly Clueless](http://www.wired.com/2015/02/lenovo-superfish/)
* [BBC News / Ad-blocking software is 'worse than Superfish'](http://www.bbc.com/news/technology-31586610)

Background / sources:

* [Extracting the SuperFish certificate](http://blog.erratasec.com/2015/02/extracting-superfish-certificate.html)
* [It's not just superfish that's the problem](https://gist.github.com/Wack0/17c56b77a90073be81d3)
* [Mirror of Komodia webpage including various software pieces](https://github.com/cryptostorm/komodia)
* [Komodia/Superfish SSL validation is broken](https://blog.filippo.io/komodia-superfish-ssl-validation-is-broken/)
* [SuperFish Removal Utility source code](https://github.com/lenovo-inc/superfishremoval)
* [Komodia rootkit findings by @TheWack0lian](https://gist.github.com/Wack0/f865ef369eb8c23ee028)
* [CERT/CC Blog: The Risk of SSL Inspection](https://www.cert.org/blogs/certcc/post.cfm?EntryID=221)
* [EFF: Dear Software Vendors: Please Stop Trying to Intercept Your Customers’ Encrypted Traffic](https://www.eff.org/deeplinks/2015/02/dear-software-vendors-please-stop-trying-intercept-your-customers-encrypted)

what?
=====

Lenovo delivered Laptops with a preinstalled Adware called Superfish in 2014.
Superfish created a severe security hole in all affected devices. Later it
turned out that several other Internet filtering products were affected by the
same issue.

The software installs a root certificate into the browser which allows
Man-in-the-Middle-attacks.

I am collecting all the software, the extracted certificates and private keys
to make sure they stay available.

Please send pull requests, mail me interesting items or upload them
[here](https://briefkasten.hboeck.de).

Hanno Böck, https://hboeck.de/
