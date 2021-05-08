# *BitXBay*

*BitXBay* is open-source and the first peer to peer decentralized online platform for trade. It is not the first supposed decentralized marketplace.  However all other such platforms currently in development are server based, at least amongst ones that have reached functional capacity. Admins are still used to monitor and potentially manipulate transactions, leaving the possibility of theft. The moderators in these other marketplaces can choose to remove goods or services. This issue is remedied in BitXBay’s marketplace through operating through the Bitmessage network.


## Bitmessage and Bitcoin

Bitmessage is a decentralized and encrypted peer to peer email communication system that can be used to send messages to one or more individuals. It was created by software developer Jonathan Warren who modeled it after cryptocurrencies and released in November 2012 under the Michigan Institute of Technology Licence. It mixes messages sent and received with the inboxes of other users to maintain identity, similar to the protocol in Dark Wallet. The software grew in popularity after June 2013, due to revelations of the American National Security Agency monitoring email activity. The system encrypts all incoming and outgoing messages through public key cryptography. This prevents anyone other than the intended receiver of the message from decrypting it. It recreates all messages inside an anonymous, peer-to-peer network, mixing all the encrypted messages of a single user with all other users on the network. Email addresses for Bitmessage are series of random letters and numbers, for the purposes of strong encryption, along with ensuring that identity cannot be tied to a Bitmessage address. Its keys are compatible with Bitcoin keys. Nodes store encrypted messages for two days before deleting them meaning no messages are archived on the network. Bitmessage also uses “Chans”, a decentralized and totally anonymous mailing list. They cannot be removed by shutting down a server, they cannot be censored, and chan messages do not contain the sender’s address or the receiver’s address. The Bitmessage network is used to send keys, transaction IDs, and communication. A special filter is created to avoid spamming, since no centralized moderator can reject or approve transactions. The filter checks all transfers to the two Bitcoin addresses owned by BitXBay, giving priority to those that involve more capital. Filters including item category and country are planned to be implemented soon, and user created categories have already been implemented.
 

## How to run BitXBay sources.
Requirements - windows xp,7,8,8.1, python 2.7 , pyqt. You can run BitXBay on linux but need to fix bitcoin-qt starting.
Copy btc folder from binaries zip file to sources folder or start your bitcoin-qt/bitcoind in server mode with rpcuser=user rpcpassword=user123 (your can change password in bitmessageqt\__init__.py) and for full funcionality you need txindex=1 in bitcoin.conf(you can use blockchain.info for download txs but it can deanonimize you)
For start run bitmessagemain.py
 
 
## BitXBay’s Infrastructure

Transactions occur in the form of escrow with multisignature addresses, with three for each transaction. One is used for the primary transaction and the other for insurance payments. The customer who initiates a transaction transfers five percent of the fee for the product or service to one of the multisignature addresses. Once a seller observes that money is transferred, he transfers five percent of the product fee of his own wealth as insurance to an address. This way, if a seller tries to cheat a buyer, his own money will be sacrificed and the same is true for a malicious buyer. If the transaction suits the buyer he signs the transaction and the five percent put forth is returned to their wallet once the transaction is completed. A single public channel exists for offers with private messages for direct communication. Bitcoin is used for payment.
Future Potential of BitXBay, Bitcoin, and decentralized systems

Arbitration in BitXbay is based solely on the insurance wallets. However, a system of Oracles could be implemented to solve disputes as well. Oracles would include groups of individuals  assigned to solve disputes between buyers and sellers with an incentive of payment if the transaction is completed or resolved. Insurance fees could go to Oracle arbitrators, with a certain percentage of both sides inputting capital that is distributed between them. This allows for a more neutral system of resolutions as opposed to bickering back in forth in private messages until a desirable transaction is forced to end due to poor diplomacy on either, or both sides or simply losing an insurance input.

Were such a system to be implemented, the ramifications of such a marketplace would be tremendous. Due to no centralized servers, it would be impossible for governments to regulate or censor such transactions. Through the use of proxies or encrypted operating systems, one could create an entirely extra-legal marketplace. This also opens the gates for international transactions, as only classification separates individuals from across the world. Were a system of contracts put in place, such as in OpenBazaar, then the same potential for arbitration-based law systems exists. Bitcoin price would rise exponentially if such an online system were polished and began to be used widely by the Bitcoin community, slowly eliminating the need for fiat based online marketplaces such as eBay, and causing wider adoption of cryptocurrencies as a whole. Bitcoin has ushered in a new era of online trading that is free from any regulation or centralization.

We hope that this will help motivate others to create anonymous and decentralized trading platforms, with the source code publicly available for editing and bug repair. This first release is only an initial alpha version and security may be an issue. The VMWare image is linked below, containing WinXP, the BitXBay client, and the blockchain for instant trading. VMWare player is needed to run the software.

[BitXBay v.1.1.4 vmware image](http://thepiratebay.se/torrent/10505247/BitXBay_v.1.4.4b_vmware_image)


## Contribute

Contributions and suggestions are welcomed at [BitXBay github repository](https://github.com/bitxbay/BitXBay).

## Support and main developer contact.



## License
(The MIT License)

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
