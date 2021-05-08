[![Logo](https://raw.githubusercontent.com/daleroberts/pypar/master/doc/logo.png)](https://raw.githubusercontent.com/daleroberts/pypar/master/doc/logo.png)

**PyPar** is a python library that provides efficient and scalable parallelism using the message passing interface (MPI) to handle **big data** and **highly computational problems**.

[![Build Status](https://travis-ci.org/daleroberts/pypar.svg?branch=master)](https://travis-ci.org/daleroberts/pypar)

**PyPar** is used by a number of large projects, such as:

 - [ANUGA shallow water equation solver](https://github.com/GeoscienceAustralia/anuga_core)
 - [TCRM A statistical-parametric model for assessing wind hazard from tropical cyclones](https://github.com/GeoscienceAustralia/tcrm)
 - [Wind multipliers: for produce wind terrain, shielding and topographic multipliers](https://github.com/GeoscienceAustralia/Wind_multipliers)

## Example

A simple 'pass the parcel' example.

```python
import pypar as pp

ncpus = pp.size()
rank = pp.rank()
node = pp.get_processor_name()

print 'I am rank %d of %d on node %s' % (rank, ncpus, node)

if rank == 0:
  msg = 'P0'
  pp.send(msg, destination=1)
  msg = pp.receive(source=rank-1)
  print 'Processor 0 received message "%s" from rank %d' % (msg, rank-1)
else:
  source = rank-1
  destination = (rank+1) % ncpus
  msg = pp.receive(source)
  msg = msg + 'P' + str(rank)
  pp.send(msg, destination)

pp.finalize()
```
