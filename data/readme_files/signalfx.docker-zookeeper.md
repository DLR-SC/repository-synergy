ZooKeeper on Docker
===================

This `Dockerfile` creates a Docker image that can be used as the base for
running ZooKeeper within a Docker container. The run script is responsible for
creating the ZooKeeper configuration based on the container's environment and
starting the ZooKeeper service.

The version of ZooKeeper is defined in the `Dockerfile` and generally points to
the latest stable release of ZooKeeper.

Environment variables
---------------------

The following environment variables are understood by the startup script to
seed the service's configuration:

  - `SERVICE_NAME` should contain the logical name of the service this
    container is an instance of;
  - `CONTAINER_NAME` should contain the logical name of the container,
    which will be used for looking up links and ports informations from the
    other environment variables. For this, the name is uppercased and
    non-alphanumeric characters are replaced by underscores.
  - `<SERVICE_NAME>_<CONTAINER_NAME>_CLIENT_PORT`, which controls the
    `clientPort` configuration setting. Defaults to 2181;
  - `<SERVICE_NAME>_<CONTAINER_NAME>_PEER_PORT`, which is used as the
    peer port specified in the server list for this node (and the
    others). Defaults to 2888;
  - `<SERVICE_NAME>_<CONTAINER_NAME>_LEADER_ELECTION_PORT`, which is
    used as the leader election port specified in the server list for
    this node (and the others).  Defaults to 3888;
  - `MAX_SNAPSHOT_RETAIN_COUNT`, the maximum number of snapshots to
    retain on disk. Defaults to to 10;
  - `PURGE_INTERVAL`, the interval, in hours, being transaction logs and
    snapshot purges. Defaults to 24 (daily).

If you plan to run a cluster of nodes, you also need to pass in the
`ZOOKEEPER_SERVER_IDS` environment variable containing a comma-separated
list of cluster nodes descriptors, as tuples of `node:id`. The `node`
part being the container name of a node, from which its coordinates can
be found.

For example, in three-node cluster, each node would expect the following
set of environment variables:

```
SERVICE_NAME=zookeeper
CONTAINER_NAME=zk-node-{0,1,2}
ZOOKEEPER_SERVER_IDS=zk-node-0:1,zk-node-1:2,zk-node-2:3
ZOOKEEPER_INSTANCES=zk-node-0,zk-node-1,zk-node-2
ZOOKEEPER_ZK_NODE_0_HOST=host1
ZOOKEEPER_ZK_NODE_0_CLIENT_PORT=2181
ZOOKEEPER_ZK_NODE_0_PEER_PORT=2888
ZOOKEEPER_ZK_NODE_0_LEADER_ELECTION_PORT=3888
ZOOKEEPER_ZK_NODE_1_HOST=host2
ZOOKEEPER_ZK_NODE_1_CLIENT_PORT=2181
ZOOKEEPER_ZK_NODE_1_PEER_PORT=2888
ZOOKEEPER_ZK_NODE_1_LEADER_ELECTION_PORT=3888
ZOOKEEPER_ZK_NODE_2_HOST=host3
ZOOKEEPER_ZK_NODE_2_CLIENT_PORT=2181
ZOOKEEPER_ZK_NODE_2_PEER_PORT=2888
ZOOKEEPER_ZK_NODE_2_LEADER_ELECTION_PORT=3888
```

This will make `zk-node-0` be ZooKeeper node ID 1 running on `host1`,
etc.

If `ZOOKEEPER_SERVER_IDS` is not specified, the container will run in
single-node mode.


Volumes
-------

The ZooKeeper images uses the following volumes that you may want to bind from
the container's host:

  - `/var/lib/zookeeper`, for the ZooKeeper data snapshots.
  - `/var/log/zookeeper`, for the ZooKeeper service logs (rotated 10
    times by 100MB sections).

Usage
-----

To build a new image, simply run from this directory:

```
$ docker build -t `whoami`/zookeeper:3.4.6 .
```

The Docker image will be built and now available for Docker to start a new
container from:

```
$ docker images | grep zookeeper
mpetazzoni/zookeeper   3.4.6              294bef30310b        2 days ago          12.29 kB (virtual 856.7 MB)
```
