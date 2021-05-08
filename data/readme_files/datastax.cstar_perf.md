# cstar_perf

cstar_perf is a performance testing platform for Apache Cassandra
which focuses on a high level of automation and test consistency.

It handles the following:

* Download and build Cassandra source code.
* Configure and bootstrap nodes on a real cluster.
* Run stress workloads.
* Capture performance metrics.
* Create reports and charts comparing different configs/workloads.
* Webserver frontend for scheduling tests, viewing prior runs, and monitoring test clusters.

## 5 Minute Introduction

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/jSS96ooZwVw/0.jpg)](http://www.youtube.com/watch?v=jSS96ooZwVw)

## Documentation

The evolving documentation is [available online here](https://datastax.github.io/cstar_perf).

* [Setup a cstar_perf development/demo environment](http://datastax.github.io/cstar_perf/setup_dev_environment.html)
* [Setup cstar_perf.tool](http://datastax.github.io/cstar_perf/setup_cstar_perf_tool.html)
* [Setup cstar_perf.frontend](http://datastax.github.io/cstar_perf/setup_cstar_perf_frontend.html)
* [Running Tests](http://datastax.github.io/cstar_perf/running_tests.html)
* [Architecture](http://datastax.github.io/cstar_perf/architecture.html)

The source for these docs are contained in the
[gh-pages](https://github.com/datastax/cstar_perf/tree/gh-pages)
branch, please feel free to make pull requests for improvements.

## License

Copyright 2014 DataStax

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

