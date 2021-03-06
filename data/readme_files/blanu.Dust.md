Dust: A Censorship-Resistant Internet Transport Protocol
Brandon Wiley
The University of Texas at Austin School of Information

Introduction
Dust is an Internet protocol designed to resist a number of attacks currently in active use to censor Internet communication. While adherence to the theoretical maxims of cryptographic security are observed where possible, the focus of Dust is on real solutions to real attacks.

Use Case
The use case for Dust assumes that there is an area of the Internet surrounded by a packet filtering firewall. All normal Internet traffic passing between the inside and outside of the zone is filtered using standard packet filtering techniques, disallowing the transmission of certain banned content. It is also assumed that there is a secure, but perhaps expensive and high latency, channel into the filtered zone. This channel is considered to be out of band, i.e. it is not over the Internet (phone, letter, messenger, etc.). Given this scenario, Dust creates an inexpensive, unfiltered channel from inside the firewall to outside.

Packet Filtering Techniques
The packet filtering techniques currently in use attempt to keep as little state as possible in order to be scalable. Filtering can happen either at the individual packet level (drop banned packets) or at the stream level (block or throttle streams containing banned packets). For stream level filtering it is common to sample only the initial packets of the stream, or to do random statistical sampling of packets. Filters do not keep persistent state about streams other than whether they have been marked as banned. Technique for defeating filtering can therefore concentrate on not sending packets which will be marked as banned.

There are two general classificiations of techniques for determining of a whether a packet is banned. Shallow packet inspection (SPI) uses just the headers of the packet. This is less expensive because the headers need to be examined anyway in order to route the packet. Deep packet inspection (DPI) simply refers to examining the packet contents as well as the headers. DPI used to be considered too expensive to be practical, but is now in widespread use by some filters.

SPI techniques in active use for marking packets are as follows: source IP and port, destination IP and port, and packet length.
DPI techniques in active use for marking packets are as follows: examing packet for connection headers and handshakes of known protocols, examining packet contents for banned static strings, and examining packet contents for banned string patterns.

How Dust Circumvents Filters
Dust is an engine for generating Internet protocols used to send packets which defeat the various filtering techniques currently in use. There is a client and a server. In order for them to communicate they must both be using the same encoding. Encodings can be devised which make traffic look random or which mimic existing protocols.

IP and port blacklists - This is outside of the scope of the protocol. Communication over the Internet requires a destination IP and port which has not been blacklisted by the filter. For the source IP and port, packet spoofing could be used. For more information on how to circumvent IP blacklists, see the Arcadia paper. http://blanu.net/Arcadia.pdf

Packet length - Dust packets have randomized lengths, shaped to a target distribution. Different encodings can make the packet lengths look random or like an existing protocol.

Connection headers and handshakes - Unlike SSH and SSL (both now filtered but some filters), Dust contains no plaintext handshake.

Static strings and string patterns - Dust packets are encrypted, therefore the contents are randomized and static strings and string patterns are removed.

Statistical properties of content - Even encrypted content can filtered, either by looking for high entropy content, or requiring that the content conform to the statistical properties of a certain protocol. After encryption, Dust content is shaped to have a statistical distribution based on a target distribution. Different encodings can make the content look random or like an existing protocol.

For further details of the mechanics of Dust, please view the documentation for either the original Dust v1 in v1/README or the newer and more advanced Dust v2 in hs/README.
