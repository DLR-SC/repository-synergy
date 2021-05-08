# jak

[![jak package on pypi](https://img.shields.io/pypi/v/jak.svg)](https://pypi.python.org/pypi/jak)
[![travis-ci](https://travis-ci.org/dispel/jak.svg?branch=master)](https://travis-ci.org/dispel/jak)
[![supported python versions](https://img.shields.io/pypi/pyversions/jak.svg)](https://pypi.python.org/pypi/jak)

jak can encrypt and decrypt files. The standard example is of a ``.env`` file with secrets in it inside of a git repository.
By sharing a key through some other means all developers can encrypt and decrypt the file, so that it is encrypted whenever it enters git history.

For a more thorough introduction you should [read the documentation.](https://jak.readthedocs.io).

jak currently works for *nix type systems such as macOS or ubuntu. We are working on windows compatibility.

**IMPORTANT!! JAK IS NOT READY FOR PRODUCTION USE YET!!**

# Installation

`pip install jak`

# Quickstart

```shell
cd ~/folderThatMayOrMayNotBeARepo
jak start
nano jakfile # add which files you want to have be encrypted.
jak encrypt all
jak decrypt all
```

One off
```shell

# Create a 64 character (32 byte) hex digit (0-f) key.
jak keygen

# Encrypt/Decrypt a specific file
jak encrypt <file> --key <key from keygen command>
jak decrypt <file> --key <key from keygen command>

# If you put the generated key in a file
jak encrypt <file> --keyfile <keyfile location>
etc.
```

# Usage

```shell
# Initialize jak (If using in git repository, make sure your cwd is the repos root)
jak start

# List the files you want to encrypt on a regular basis.
nano jakfile

# Encrypt/Decrypt all of the files that are specified as
# "files_to_encrypt" in your jakfile.
jak encrypt all
jak decrypt all

# Don't need to pass key (--key) because it defaults to keyfile designated
# in the jakfile
jak encrypt <specific file>
jak decrypt <specific file>

# Generate a strong key. An encryption is only as strong as the key.
# ALWAYS use a strong 32 character key.
jak keygen

# Where action is one of encrypt/decrypt
# Overrides the key the jakfile may be pointing to.
jak <action> -k faca44c66af094f18e3e69eaf2328e557a618ca0e3d560a5f83c6f43a172b542

# Overrides the key in the jakfile with a key from a file
jak <action> -kf <keyfile>

# We highly recommend you read the jak --help man texts.
jak --help

# It works for specific commands as well
jak keygen --help
```

# Authors

jak is stewarded by [Dispel](https://dispel.io) but all of the [contributors](https://github.com/dispel/jak/graphs/contributors) are the authors.

# License (Apache-2.0)

see [LICENSE](https://github.com/dispel/jak/blob/master/LICENSE) file.
