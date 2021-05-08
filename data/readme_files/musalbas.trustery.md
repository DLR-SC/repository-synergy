# trustery
**Note: this is an experimental prototype and shouldn't be used in production. Feedback welcome.**

Trustery is a Public Key Infrastructure (PKI) and identity management system on the Ethereum blockchain.

The aim of this project is to provide a PKI that has built-in certificate transparency to make it easy to detect rogue certificates, by building an alternative to decentralized PKI by using a public-ledgered web-of-trust model for fine-grained identity management.

This project is a result of my [undergraduate thesis](https://github.com/musalbas/trustery-report/blob/master/Report.pdf).

## Command-line options
<pre>Usage: trustery [OPTIONS] COMMAND [ARGS]...

  Ethereum-based identity system.

Options:
  --help  Show this message and exit.

Commands:
  add                 Add an attribute to your identity.
  ipfsadd             Add an attribute to your identity over IPFS.
  ipfsaddpgp          Add a PGP key attribute to your identity over IPFS.
  retrieve            Retrieve an attribute.
  revoke              Revoke one of your signatures.
  search              Search for attributes.
  sign                Sign an attribute.
  trust               Trust an Ethereum address.
  trusted             View the list of trusted Ethereum addresses.
  untrust             Untrust an Ethereum address.
</pre>

## Installation
```
git clone https://github.com/musalbas/trustery.git
cd trustery/pytrustery
pip install --user --editable .
```

You can now run the command `trustery` from the command-line.

In order to use the system, you will first need to:
* Run geth with the JSON RPC enabled.
* Compile and publish the smart contract at `contract/trustery-alt.sol` and change the `TRUSTERY_DEFAULT_ADDRESS` variable in `pytrustery/ethapi.py`.

As this project is currently experimental, there is no official smart contract published yet. You are advised to test the smart contract on a test network.

At the moment, all transactions are executed from your first Ethereum address (`eth.accounts[0]`).
