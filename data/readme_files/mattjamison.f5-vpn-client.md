F5 VPN Command-line client.

This software allows you to connect to an F5 VPN server without using their
browser plugin. It also has the advantage of setting up DNS properly on OSX
systems, which the official client doesn't do. (but maybe they will in the
future, now that they can copy the method I use).

It is not supported or affiliated with F5 in any way. I actually find it rather
sad the client they provide is so terribly poor that I had to write this in
order to get reliable access to my company's VPN.

This software does not require any software from F5 to be installed on the
client. The only requirement is Python 2.3.5 or later. It works on at least
Linux and OSX systems, but porting to any similar OS should be trivial. Porting
to Windows, on the other hand, is probably not reasonably possible.

To install:
"make install" as root.

To run:

"f5vpn-login user@host" (not as root).

(user@host is saved for future invocations, so doesn't need to be
specified on future invocations)

Have fun,
James Y Knight, <foom@fuhm.net>

ChangeLog
---------
2012-10-11
 - Added ability to choose the VPN connection when multiple are returned

2008-12-06
 Features:
 - Added SOCKS proxy support, if you have the "SocksiPy" python module
   installed; use the --socks5-proxy argument.

 Bugfixes:
 - Fixed compatibility issues with some newer version of the VPN server.
   (thanks James Trammell and Dave Cadwallader)

2008-10-31
 Bugfix:
 - Oops I broke resolvconf again. :( Forgot an os.close()...

2008-10-25
 Bugfixes:
 - Support non-split-tunneling VPN configuration. (thanks Mark Kamichoff)
   - Use "UseDefaultGateway0" param to tell pppd to set the machine's default
     route, and to override the DNS servers, rather than supplementing them.
   - Allow LAN0 to be empty.
 - Don't attempt to reuse a session when the old session is from a different
   user/server.
 - Handle VPN servers with "pre-login-checks" configured. (thanks to Kazuyuki
   Saito).
 - Due to a typo, resolvconf wasn't being used on linux even when present.
   (Thanks Fare and others)
 - Fix crash in routespec_to_revdns when getting a /32 route.
 - Miscellaneous other cleanups

2008-08-04
 Features
 - Added ability to connect via a HTTPS proxy with a --proxy=hostname:port argument.

2008-07-25
 Features:
 - Basic functionality on iPhone v2.0. Requires python and pyobjc, both of which
   you can install easily via Cydia. For now, at least, you'll have to run it in
   the terminal, and, since the iphone drops the net connection every time the
   phone sleeps, it's not really very usable.

2008-07-21
 Bugs:
 - Fixed bug in DNS on linux. (too clever by far)
 - Retry connecting a few times if the VPN fails to answer properly.

2008-05-07
 Features:
 - Added support for the resolvconf DNS-manager on linux systems which have it installed.

 Bugs:
 - Made the netmask parser more forgiving, since apparently some people have
   their vpn servers set up oddly.
 - If no DNS0 parameter is supplied by the VPN server, don't attempt to set up
   DNS overrides.

2008-01-17
 Features:
 - Added a SIGUSR1 handler which prints some stuff.

 Bugs:
 - Fixed a bug that caused it to not work on OSX 10.4.
 - Make the keepalive feature actually work.

2007-12-07:
 New features:
 - Now sends a little traffic over the connection at least every 5 minutes, to
   keep crappy home NAT devices from tearing down the TCP connection.  (NetGear,
   with your 10 minute inactivity timeout...I'm looking at you, with disgust.)
 - On OSX 10.5, make reverse DNS of VPN-remote IPs work right (this is only an
   issue on OSX to begin with, as linux doesn't support split-DNS anyhow.)

 Bugs:
 - Fixed bug with the way I called SSL_write causing "bad write retry" errors occasionally.
 - On OSX 10.5, use the SystemConfiguration python module instead of execing
   scutil (revdns change runs afoul of scutil's 256char line limit).

2007-10-24:
 - Don't assume the VPN ID is 0,4: actually read the page to find the right number.

2007-09-08:
  Rewrote the f5vpn-login script to no longer require the "svpn" binary
  from F5. It now just requires python and a little platform-specific
  knowledge about setting up routes and dns (implemented for linux and
  osx, currently, feel free to contribute others).

  Bonus: it works better now too:
  - It actually shuts down the connection when you ask it to.
  - On OSX, it uses the platform specific DNS setup features, which
	allows the dns information to not be overwritten periodically.
