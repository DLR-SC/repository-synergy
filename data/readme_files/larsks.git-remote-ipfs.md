This is a [gitremote helper][] permitting git to clone from and push
to [ipfs][].  Note that while it works in principal, it is only mildly
useful until such time as the ipfs project introduces support for
publishing multiple names via ipns.

[gitremote helper]: https://www.kernel.org/pub/software/scm/git/docs/gitremote-helpers.html
[ipfs]: http://ipfs.io/

## INSTALLATION

You can install this module directly using `pip`, like this:

    pip install git+https://github.com/larsks/git-remote-ipfs

You can of course also clone it and run `setup.py` instead.

## SPECIFYING AN IPFS REMOTE

### Using IPFS style paths

Because paths like `/ipfs/HASH` look just like filesystem paths, we
need to explicitly tell git to use an ipfs remote by prefixing the
path with `ipfs::`, like this:

    git clone ipfs::/ipfs/HASH myproject

The code is able to resolve ipns names, so this will also work:

    git clone ipfs::/ipfs/HASH myproject

Note that ipns support is effectively useless right now, until it
becomes possible to publish more than a single name per client.

### Using IPFS URLs

This code also supports a URL format for ipfs remotes.  For explicit
hashes (the equivalent of `/ipfs/HASH`), the format is:

    ipfs:///HASH

So:

    git clone ipfs:///HASH

For ipns names, the format is:

    ipfs://HASH

Yes, the difference is a single `/`.  This will probably changed, based on the discussion in [issue 1678][].

[issue 1678]: https://github.com/ipfs/go-ipfs/issues/1678

## EXAMPLE USAGE

### Pushing to ipfs

    $ git remote add ipfs ipfs::
    $ git push ipfs master
    WARNING:git_remote_ipfs.remote:new repository hash = QmctS8mbpdQ1rgvS9SdFfJsoAE8s97FdXDHJQtobewAXKG
    To ipfs::
     * [new branch]      master -> master

### Cloning from ipfs

To clone from ipfs the repository pushed in the previous example:

    $ git clone ipfs::/ipfs/QmctS8mbpdQ1rgvS9SdFfJsoAE8s97FdXDHJQtobewAXKG myproject

## KNOWN BUGS

The support for ipns references is completely untested at this point.
While an initial clone from an ipns name should work, there is no code
for updating the name with a new HEAD when pushing changes.

## DEBUGGING

You can enable verbose debugging by setting `GIT_IPFS_LOGLEVEL=DEBUG`
in your environment.

### LICENSE

git-remote-ipfs -- a gitremote helper for ipfs  
Copyright (C) 2015 Lars Kellogg-Stedman

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

