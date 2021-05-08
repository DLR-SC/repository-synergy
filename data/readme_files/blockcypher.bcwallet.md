bcwallet
========

Use at your own risk. We recommend starting with BlockCypher testnet coins (`free faucet here <https://accounts.blockcypher.com/blockcypher-faucet>`_).

Installation
------------

To get started:

.. code-block:: bash

    pip install bcwallet
    bcwallet

(then follow the instructions on the screen)

If you don't have `pip` pre-installed on your machine you can `install pip here <http://pip.readthedocs.org/en/stable/installing/>`_. If for some reason `pip` doesn't work you can use `easy_install`, but `you really shouldn't do that <http://stackoverflow.com/questions/3220404/why-use-pip-over-easy-install>`_.

Note that if you use an outdated version of pip you may get a scary ``InsecurePlatformWarning`` warning installing any package (including ``bcwallet``). As always, you should upgrade your pip to the latest version before installing any new software:

.. code-block:: bash

    pip2 install --upgrade pip

If `pip2` doesn't work, try `pip` instead.

Advanced users can download the source code and build from source:

.. code-block:: bash

    python setup.py build
    python setup.py install


FAQs
----

**Q: There are lots of wallets out there, what makes bcwallet unique?**

A: bcwallet is:

- **Multi-Currency**: Supports Bitcoin (and Testnet), Litecoin, Dogecoin, and BlockCypher Testnet.
- **Nearly Trustless**: Keys and signatures are generated locally for trustless use.
- **No Key Pool**: The seed is not stored locally, the app is booted with the user supplying the master key so the filesystem is never used.
- **Hard to Mess Up**: As long as you don't lose or share your master private key, everything else is simple.
- **Accurate Transaction Fees**: Smart calculation lets user decide how long until their transaction will make it into a block.
- **Airgap Usage**: Can be booted with the public key in watch-only mode, which is great for fetching transaction info to sign offline with a more secure machine.
- **Very Few LoC**: Blockchain heavy lifting powered by BlockCypher, which leads to massive reduction in client-side code used for ease of auditing.


**Q: Why is an HD wallet important?**

A: The best practice in bitcoin is to `use a new address for every transaction <https://bitcoin.org/en/protect-your-privacy>`_ (including the change address your wallet specifies when you send funds to someone else). This is for both personal/network privacy as well as clarity in determining who has paid you.

Addresses correspond to private keys and are free to create, but the private key used to create an address must be saved or those funds will be lost forever. This creates a difficult key management problem, as each transaction means you have to store a new key. If you backup your keypool today and then do a bunch of transactions tomorrow (which your wallet generates new keys for), those new keys will not be included in your original backup. You could have a diligent backup and still lose funds!

All of these problems are solved with HD wallets. Just backup your master private key once and you're set forever.

HD wallets are essential, and you really shouldn't use any wallet that isn't HD (``<cough>blockchain.info</cough>``).

**Q: Does BlockCypher ever see my private keys?**

A: No! We never see your private keys. Keys are generated locally, and transactions are signed locally as well. Once you sign a transaction locally, by definition it cannot be edited and does not reveal your private key. When you send that to BlockCypher, BlockCypher relays it to the rest of the network quickly using its extremely well-connected nodes.


**Q: What bad things could happen if I use this wallet?**

A: While BlockCypher can't steal your funds, every wallet has a security/convenience tradeoff. Here are bcwallet's:

- **BlockCypher has your extended public key and can easily use that to figure out which addresses you control**, which is bad for your privacy. We don't ask for a name or email address to use the wallet, but unless you're connected to the internet using Tor we could see your IP address.
- **BlockCypher could suffer from downtime**, which would make bcwallet fairly worthless: you wouldn't be able to fetch your balance, transaction history, unspent transaction outputs, or broadcast transactions. However, you can always dump your private keys and addresses (using option 0 on the home screen) to spend your funds with *any* bitcoin wallet. If a wallet supported importing a master private key (hopefully more will in the future), you could just import that one string.
- **BlockCypher could trick you into paying a large transaction fee** (to whatever miner mined your transaction, not to BlockCypher). Since bcwallet relies on BlockCypher to fetch how much bitcoin each address controls (the UTXOs), if BlockCypher were to under-report it could cause bcwallet to mis-calculate the transaction fee. BlockCypher has no incentive to do this of course, and was built to solve this very problem.

**Q: What path for key derivation do you use? BIP32 default wallet layout? BIP39? BIP44?**

A: We use a simple derivation with m/0/k for the external chain (receiving addresses) and m/1/k for the internal chain (change addresses). BIP44 uses hardened derivation for these chains, which means your master public key is completely useless, and one core feature of bcwallet is that you can boot the wallet using just an extended *public* key (very useful for airgapping and signing transactions offline). bcwallet's simplified choice of tree traversal also makes it much harder to lose funds by losing track of them during traversal. Since after traversing to the 0th account, BIP32 and BIP44 are almost identical implementations, we may add support for those wallets in the future.


**Q: Why is this this app designed to work with python2 only?**

A: python3 is great, but but there are a few reasons why python 2 is better for this case:

- Most operating systems comes with python2 pre-installed, not python3.
- Python3 unicode handling causes problems, `Armin Ronacher strongly recommends python2 for command line apps <http://click.pocoo.org/4/python3/>`_.

**Q: Can I submit a pull request to bcwallet?**

A: Absolutely! If you'd like to edit bcwallet, here's the best way to install it on your machine in a virtual environment:

.. code-block:: bash

    git clone https://github.com/blockcypher/bcwallet.git
    cd bcwallet
    virtualenv --python=python2 venv  # see python2 note above
    source venv/bin/activate
    pip install --editable .
    bcwallet


Uninstallation
--------------

So sad to see you go! Just enter the following and be on your way:

.. code-block:: bash

    pip uninstall bcwallet

(then confirm your uninstallation at the prompt)

If you really want a clean install/uninstall, first create a virtual environment (see PR instructions for details). Then the install will be contained in the virtual environment.


Acknowledgements
----------------

This wallet is built using:

- BlockCypher's very powerful `bitcoin API <http://www.blockcypher.com/>`_. It supports features that other APIs don't, and not only makes this wallet possible but massively reduces the amount of client-side code written.
- Steven Buss' very awesome `bitmerchant <https://github.com/sbuss>`_ library for generating keys
- Vitalik Buterin's `pybitcointools <https://github.com/vbuterin/pybitcointools>`_ for ecdsa signatures and decoding raw bitcoin transactions
