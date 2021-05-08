# rpm-s3

This small tool allows you to maintain YUM repositories of RPM packages on S3. The code is largely derived from [s3yum-updater](https://github.com/rockpack/s3yum-updater).

The advantage of this tool is that it does not need a full copy of the repo to operate. Just give it the new package to add, and it will just update the repodata metadata, and upload the given rpm file.

If you're looking for the same kind of tool, but for APT repositories, I can recommend [deb-s3](https://github.com/krobertson/deb-s3).

## Requirements

1. You have python installed (2.6+).

1. You have your S3 credentials available in the `AWS_ACCESS_KEY` and `AWS_SECRET_KEY` environment variables:

        export AWS_ACCESS_KEY="key"
        export AWS_SECRET_KEY="secret"

## Installation

    git clone https://github.com/crohr/rpm-s3 --recurse-submodules

## Usage

Let's say I want to add a `my-app-1.0.0.x86_64.rpm` package to a yum repo hosted in the `yummy-yummy` S3 bucket, at the path `centos/6`:

    ./bin/rpm-s3 -b yummy-yummy -p "centos/6" my-app-1.0.0.x86_64.rpm

## Testing

Use the provided `/test/test.sh` script:

    vagrant up
    vagrant ssh
    AWS_ACCESS_KEY=xx AWS_SECRET_KET=yy BUCKET=zz ./test/test.sh

Also:

    ./bin/rpm-s3 -b s3-bucket -p "centos/6" --sign my-app-1.0.0.x86_64.rpm

    echo "[myrepo]
    name = This is my repo
    baseurl = https://s3.amazonaws.com/yummy-yummy/centos/6" > /etc/yum.repos.d/myrepo.repo

    yum makecache --disablerepo=* --enablerepo=myrepo

    yum install --nogpgcheck my-app

## Troubleshooting

### Requirements if you want to sign packages

Have a gnupg key ready in your keychain at `~/.gnupg`. You can list existing secret keys with `gpg --list-secret-keys`

Have a `~/.rpmmacros` file ready with the following content:

    %_signature gpg
    %_gpg_name Cyril Rohr # put the name of your key here

Pass the `--sign` option to `rpm-s3`:

    AWS_ACCESS_KEY="key" AWS_SECRET_KEY="secret" ./bin/rpm-s3 --sign my-app-1.0.0.x86_64.rpm

### Import gpg key to install signed packages

    sudo rpm --import path/to/public/key # this also accepts URLs

## TODO

* Release as python package.
* Add spec and control files for RPM and DEB packaging.
