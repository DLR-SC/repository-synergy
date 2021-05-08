# apt-boto-s3

[![Build Status](https://travis-ci.org/lucidsoftware/apt-boto-s3.svg?branch=master)](https://travis-ci.org/lucidsoftware/apt-boto-s3)
[![Package](https://img.shields.io/bintray/v/lucidsoftware/apt/apt-boto-s3.svg)](https://bintray.com/lucidsoftware/apt/apt-boto-s3/_latestVersion)

The *fast* and *simple* S3 transport for apt. Access S3-hosted apt repositories via the AWS APIs.

## Why apt-boto-s3?

While there are alternative apt transports for S3, like [apt-transport-s3](https://github.com/BashtonLtd/apt-transport-s3) or [apt-s3/apt-transport-s3](https://github.com/castlabs/apt-s3), this project has

* standard AWS credential resolution, including environment variables and ~/.aws/credentials
* pipelining requests for faster updates
* Last-Modified caching
* broad AWS API support, e.g. v4 credentials
* operability with any S3-compatible API
* works with all standard digest algorithms
* Apache 2.0 license

## Install

Install from the APT repository:

```
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 379CE192D401AB61
echo deb http://dl.bintray.com/lucidsoftware/apt/ lucid main > /etc/apt/sources.list.d/lucidsoftware-bintray.list

apt-get update
apt-get install apt-boto-s3
```

## Usage

### URLs

The URL in apt sources can have any of the formats [documented](http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html#access-bucket-intro) by AWS.

```
# path style
deb s3://s3.amazonaws.com/my-bucket jessie main contrib

# path style for region other than us-east-1
deb s3://s3-sa-east-1.amazonaws.com/my-bucket jessie main contrib

# virtual-hosted style
deb s3://my-bucket.s3.amazonaws.com jessie main contrib
```

Any endpoint can be used that has an S3-compatible API.

```
deb s3://swift.example.com/my-bucket jessie main contrib
```

### Credentials

apt-boto-s3 resolves AWS credentials in the usual manner.

1. Environment variables: `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
1. Credentials file: `~/.aws/credentials`
1. Instance metadata: http://169.254.169.254

Credentials may be also be specified in in the [user information](https://tools.ietf.org/html/rfc3986#section-3.2.1) of the URL. The key and secret should be [URL-encoded](https://tools.ietf.org/html/rfc3986#section-2.1).

```
deb s3://AWS_ACCESS_KEY:AWS_SECRET_KEY@my-bucket.s3.amazonaws.com jessie main contrib
deb s3://AKIAIOSFODNN7EXAMPLE:wJalrXUtnFEMI%2FK7MDENG%2FbPxRfiCYEXAMPLEKEY@my-bucket.s3.amazonaws.com jessie main contrib
```

URL credentials take precendent when present.

#### Signature version

Hopefully, this should "just work" and you can ignore this.

Some regions, e.g. eu-central-1, support only AWS version 4 signatures. However, version 4 does not work with virtual-hosted style URLs, and many S3 clones support only version 2.

apt-boto-s3 uses version 4 for path style URLs with a s3*.amazonaws.com host; otherwise it uses version 2.

If you need to override this default, set `S3::Signature::Version` in apt configuration, e.g. in `/etc/apt/apt.conf.d/s3`:

```
S3::Signature::Version "2";
```

### Instance metadata service

You can also tweak the timeout and retry settings for requests to retrieve credentials from the instance metadata.

```
S3::MetadataService::Retries "5";
S3::MetadataService::Timeout "2";
```

The default values are 5 retries with a 1 second timeout.

## Build

To build and install from source,

```sh
make
make install # as root
```
