# LASER-ethereum
![Master Build Status](https://img.shields.io/circleci/project/github/b-mueller/laser-ethereum/master.svg)
![PyPI version](https://img.shields.io/pypi/v/laser-ethereum.svg)

LASER is a symbolic virtual machine (SVM) that runs Ethereum smart contracts. It accurately models most features of the Ethereum virtual machine including inter-contracts calls.

## Installing and Running the Symbolic Virtual Machine

The SVM runs Mythril `Disassembly` objects instead of raw Ethereum bytecode. It is therefore best installed alongside with [Mythril](https://github.com/ConsenSys/mythril). Since mythril only supports python 3, we also requires python 3 here.  

```
$ pip3 install mythril
```

The `Disassembly` object can be created from Solidity source code or Ethereum bytecode.

```
from laser.ethereum import svm
from mythril.ether.soliditycontract import SolidityContract
contract = SolidityContract("solidity_examples/underflow.sol", "Under")

disassembly = contract.disassembly
```

It contains a list of instructions in the format `{'address': address, 'opcode': mnemonic, 'argument': argument}`.

```
>>> disassembly.instruction_list
[{'address': 0, 'opcode': 'PUSH1', 'argument': '0x60'}, {'address': 2, 'opcode': 'PUSH1', 'argument': '0x40'}(...)
```

To run the code in the symbolic VM it must be mapped to virtual contract accounts. Each account is constructed with an Ethereum address and a `Disassembly` object (the contract code), plus an optional contract name. The LASER constructor expects a mapping of addresses to account objects. 

```
address = "0x0000000000000000000000000000000000000000"
account = svm.Account(address, disassembly, "Under")
accounts = {address: account}
```

Once initialized, symbolic execution is started with the `sym_exec(entry_address)` method. The `entry_address` argument specifies the contract to be used as the entrypoint (the other mapped contracts are made available for message calls).


```
laser = svm.LaserEVM(accounts)
laser.sym_exec("0x0000000000000000000000000000000000000000")
```

## Inspecting Program States

LASER returns an object containing the state space of the smart contract organized as a graph. Each node in the graph represents a basic block of code being executed, and contains a list of global states - one state for each program counter position. Every node also has an associated set of constraints. A list of edges between nodes along with the constraint on each edge is also provided. This can be used to [draw a control flow graph](https://github.com/ConsenSys/mythril#control-flow-graph).

Each node contains a list of state objects, each of which contains the complete global state during that point in execution (PC address).

```
>>> node = laser.nodes[0]
>>> node.states
[<laser.ethereum.svm.GlobalState object at 0x1064a4a58>, <laser.ethereum.svm.GlobalState object at 0x1064a4b70>, (...)]
```

### The State Object

The state object representes the global system state. It contains an address-to-account mapping, an environment object, and a machine state object. Each account has an associated `storage` dict with a mapping of storage slots to data (this is filled with symbolic and concrete entries during execution).

```
>>> state = node.states[0]
>>> state.accounts['0x0000000000000000000000000000000000000000'].as_dict()
{'nonce': 0, 'code': <mythril.disassembler.disassembly.Disassembly object at 0x106413940>, 'balance': balance, 'storage': {}}
```

The structure of the machine state and execution environment is largely identical to the specification in the [yellow paper](https://github.com/ethereum/yellowpaper).

#### Machine state (μ)

```
The machine state μ is defined as the tuple (g, pc, m, i, s) which are the gas available, the program counter pc ∈ P256, the memory contents, the active number of words in memory (counting continuously from position 0), and the stack contents. The memory contents μm are a series of zeroes of size 256.
```

In LASER:

```
>>> state.mstate.as_dict()
{'pc': 0, 'stack': [], 'memory': [], 'memsize': 0, 'gas': 10000000}
```

#### Execution Environment (I)

```
- Ia, the address of the account which owns the code that is executing.
- Io,thesenderaddressofthetransactionthatorig- inated this execution.
- Ip, the price of gas in the transaction that origi- nated this execution.
- Id, the byte array that is the input data to this execution; if the execution agent is a transaction, this would be the transaction data.
- Is, the address of the account which caused the code to be executing; if the execution agent is a transaction, this would be the transaction sender.
- Iv, the value, in Wei, passed to this account as part of the same procedure as execution; if the execution agent is a transaction, this would be the transaction value.
- Ib, the byte array that is the machine code to be executed.
- IH , the block header of the present block.
- Ie, the depth of the present message-call or contract-creation (i.e. the number of CALLs or CREATEs being executed at present).
```

In LASER:

```
>>> state.environment.as_dict()
{'active_account': <laser.ethereum.svm.Account object at 0x1064a4780>, 'sender': caller, 'calldata': [], 'gasprice': gasprice, 'callvalue': callvalue, 'origin': origin, 'calldata_type': <CalldataType.SYMBOLIC: 2>}
>>>
```

#### Path Constraints

Each node has a list of associated path constraints that can be passed to the Z3 Solver.

```
>>> for c in node.constraints:
...     print(z3.simplify(c))
... 
ULE(4, calldatasize_Under)
Not(Extract(255, 224, calldata_Under_0) == 404098525)
Not(Extract(255, 224, calldata_Under_0) == 1648476113)
Not(Extract(255, 224, calldata_Under_0) == 1889567281)
Extract(255, 224, calldata_Under_0) == 2736852615
callvalue == 0

```

## For developers

You can find how to run tests and generate coverage reports in [README_DEV.md](./README_DEV.md)

## Caveats

- Gas usage is not yet fully simulated
- Native contracts are not yet implemented

## What does LASER stand for?

[Light amplification by stimulated emission of radiation](https://en.wikipedia.org/wiki/Laser). The sole reason for calling this software LASER was so there could be a method called `fire_lasers`.


