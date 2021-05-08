<!---
  Licensed to the Apache Software Foundation (ASF) under one
  or more contributor license agreements.  See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership.  The ASF licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing,
  software distributed under the License is distributed on an
  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
  KIND, either express or implied.  See the License for the
  specific language governing permissions and limitations
  under the License.
-->
# clusterdock

## Overview
*clusterdock* is a framework for creating Docker-based container clusters. Unlike regular Docker
containers, which tend to run single processes and then exit once the process terminates, these
container clusters are characterized by the execution of an init process in daemon mode. As such,
the containers act more like "fat containers" or "light VMs;" entities with accessible IP addresses
which emulate standalone hosts.

## Usage
The *clusterdock* framework has been designed to be run out of its own container while affecting
operations on the host. To do this, the framework is started by invoking `docker run` with an option
of `-v /var/run/docker.sock:/var/run/docker.sock` required to ensure that containers launched by the
framework are started on the host machine. To avoid problems that might result from incorrectly
formatting this framework invocation, a Bash helper script (`clusterdock.sh`) can be sourced on a
host that has Docker installed. Afterwards, invocation of any of the binaries intended to carry
out *clusterdock* actions can be done using the `clusterdock_run` command. As an example, assuming
Docker is already installed and the working directory is the root of this Git repository:
```
source ./clusterdock.sh
clusterdock_run ./bin/start_cluster cdh --help
```
