# MinaOTP-Shell

MinaOTP-Shell is a two-factor authentication tool that runs in a terminal as a command-line tool.

This command-line tool will generate secure dynamic 2FA tokens for you, the `add`, `remove`, `list`, `show` and `import` will be pretty convenient in the terminal.

### Installation

```shell
pip install minaotp
```

### Usage

* Help information

```shell
$ mina -h
usage: mina [-h] {list,add,remove,show,import} ...

MinaOTP is a two-factor authentication tool that runs in the terminal

positional arguments:
  {list,add,remove,show,import}
                        Available commands
    list                List all tokens.
    add                 Add a new token.
    remove              Remove a token.
    show                Show a token on-time
    import              Import tokens from a local json file

optional arguments:
  -h, --help            show this help message and exit
```

* List all tokens

```shell
$ mina list
=OID== =====ISSUER===== =====REMARK===== ======OTP=======
  0          test             test            904540
  1         hello            world            344962
  2          mina             otp             032218
```

* Add a new token

```shell
$ mina add -h
usage: mina add [-h] --secret SECRET --issuer ISSUER --remark REMARK

optional arguments:
  -h, --help       show this help message and exit
  --secret SECRET  Secret info to generate otp object.
  --issuer ISSUER  Issuer info about new otp object.
  --remark REMARK  Remark info about new otp object.
```

* Remove a token

```shell
$ mina remove -h
usage: mina remove [-h] oid

positional arguments:
  oid         oid of the token

optional arguments:
  -h, --help  show this help message and exit
```

* Show a token on-time

```shell
$ mina show 2
=OID== =====ISSUER===== =====REMARK===== ======OTP=======
  2          mina             otp             983418
```

* Import tokens from a local json file

```shell
$ mina import -h
usage: mina import [-h] file_path

positional arguments:
  file_path   path of the local json file

optional arguments:
  -h, --help  show this help message and exit
```

### Todos

- [x] import tokens from a local json file
- [ ] export all tokens to a local json file