# IPFS Consortium

A agreement among trusted parties to assist with persistance of IPFS objects.


# How To Use

## Clone the source

```
$ git clone https://github.com/pipermerriam/ipfs-persistence-consortium.git
```

`cd` into the newly cloned repository

## Install Requirements

You can do this with pip.  Recommended to do this in a virtual environment

```
$ pip install -r requirements.txt
```

## Setup a config file

Setup a `config.json` in the root directory of the project that looks like the
following.

```javascript
{
    "peers": [
        "QmP24Zx4uEh1ZhmPsERb4ZwBDVdXjHiFqRSkHyqeSJQEsW"
    ]
}
```

The `peers` key needs to be an array of IPFS ids.


## Run the script

```bash
$ python ipfs_consortium.py
```

This will loop through all of the peers and pin their files locally.  This
script can be setup to run periodically with something like `cron`.


# How it works

1. For each peer in the `peers` list, the script uses `ipfs name resolve` to
   find the ipfs address that has been published from that peer.
2. This address is expected to point to a directory of JSON files.  Each of
   these json files should contain a top level array of IPFS hashes.  These hashes
   represent the files that this peer wishes to have mirrored.
3. Each of these hashes is **pinned**.

# How to ask others to mirror your IPFS content

Create a directory to contain your IPFS manifest JSON files.

```bash
$ mkdir ~/ipfs-manifests
```

In this directory, create any number of `*.json` files.  These files should contain a single top level array of IPFS file hashes.

```javascript
// manifest1.json
[
    "QmYwxuzozCBSD3FLP5Rg1pAXA4qjDtNrdGjyNzqEtr8TKu",
    "QmTrXyK24CAymWj5eATjxrisc8QaJocnGSY11BFFDEvqtH"
]
```

Add this file into IPFS

```bash
$ ipfs add -r ipfs-manifests
added QmPSM44WZ6rFW7d81pMQYG7BzDJRjhrWh7s69dTUpgmtRY ipfs-manifests/manifest-1.json
added QmbsC66VNjNdBU8simUfmxj2dUdpyWgkJKRiVBxBE9sBXQ ipfs-manifests
```

Take the hash associated with the `~/ipfs-manifests` directory and publish it
on IPNS

```bash
$ ipfs name publish QmbsC66VNjNdBU8simUfmxj2dUdpyWgkJKRiVBxBE9sBXQ
Published to QmP24Zx4uEh1ZhmPsERb4ZwBDVdXjHiFqRSkHyqeSJQEsW: QmbsC66VNjNdBU8simUfmxj2dUdpyWgkJKRiVBxBE9sBXQ
```

Give other members your IPFS id and ask them to add it to their `peers` list.
You can get this your IPFS id with:

```bash
{
    "ID": "QmfGr14Jmu3fUvN74MGG7C8Av8buDbtLVK7Bs4yiaS4chX",
    "PublicKey": "CAASpgIwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCQxRzWJvimlHD0sHY8+n5X4TYhj2tNLVfiJZLJz1vZRMwSTqgmMyrFEh2o+4B21EtfR6tf0eKLwUerfPR0DUWRjJv4YL1+SidNxESsqIaENPBsaLwhGRFXM3PYeW+UjlTjrEybOf2cCY1h8+9XrlCMLHPROzS+QHbAW4Elz7CfqmbMbhDVXEuIVkDQxvXPVgVQEFwkKYexwfHbeLa2n5WTunsSec6GlEUfbwQOlmb/iMYfu2HfPztmwS1wXk1d4WvsUiB53gqljp7jsTPaE5YD4wyyUlQDeulO1zCdDjq2gQDxjtZ0fUzLfJU3dsdnpPcP1KQzvvSEAxNedjAsRRQTAgMBAAE=",
    "Addresses": [
        "/ip4/127.0.0.1/tcp/4001/ipfs/QmfGr14Jmu3fUvN74MGG7C8Av8buDbtLVK7Bs4yiaS4chX",
        "/ip4/10.0.1.48/tcp/4001/ipfs/QmfGr14Jmu3fUvN74MGG7C8Av8buDbtLVK7Bs4yiaS4chX"
    ],
    "AgentVersion": "go-ipfs/0.4.0-dev",
    "ProtocolVersion": "ipfs/0.1.0"
}
```

# Setting up an EC2 instance running ipfs

[EC2_setup.md](EC2_setup.md)
