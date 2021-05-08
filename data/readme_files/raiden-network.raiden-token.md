# Raiden Token

## Smart Contracts, Unittests and Infrastructure.

### Installation

#### Prerequisites

 * Python 3.6
 * [pip](https://pip.pypa.io/en/stable/)

#### Setup

 * pip install -r requirements.txt

#### Usage

```sh

# compilation
populus compile

# tests
pytest -p no:warnings -s
pytest tests/test_auction.py -p no:warnings -s

# Recommended:
pip install pytest-xdist
pytest -p no:warnings -s -n NUM_OF_CPUs

```

#### Deployment


##### Chain setup

 * `privtest`
   - start:
   ```
   geth --ipcpath="~/Library/Ethereum/privtest/geth.ipc" --datadir="~/Library/Ethereum/privtest"  --dev  --rpccorsdomain '*'  --rpc  --rpcport 8545 --rpcapi eth,net,web3,personal --unlock 0xf590ee24CbFB67d1ca212e21294f967130909A5a --password ~/password.txt

   # geth console
   # you have to mine yourself: miner.start()
   geth attach ipc:/Users/user/Library/Ethereum/privtest/geth.ipc
   ```

 * `kovan`
   - change default account: [/populus.json#L189](/contracts/populus.json#L189)
   - start https://github.com/paritytech/parity
   ```
   parity --geth --chain kovan --force-ui --reseal-min-period 0 --jsonrpc-cors http://localhost --jsonrpc-apis web3,eth,net,parity,traces,rpc,personal --unlock 0x5601Ea8445A5d96EEeBF89A67C4199FbB7a43Fbb --password ~/password.txt --author 0x5601Ea8445A5d96EEeBF89A67C4199FbB7a43Fbb
   ```
 * `ropsten`
   - change default account: [/contracts/populus.json#L52](/contracts/populus.json#L52)
   - start:
   ```
   geth --testnet --rpc  --rpcport 8545 --unlock 0xbB5AEb01acF5b75bc36eC01f5137Dd2728FbE983 --password ~/password.txt

   ```

 * `rinkeby`
   - https://www.rinkeby.io/ (has a Faucet)
   - change default account: [/contracts/populus.json#L224](/contracts/populus.json#L224)
   - start:
   ```
   # First time
   geth --datadir="~/Library/Ethereum/rinkeby" --rpc --rpcport 8545 init ~/Library/Ethereum/rinkeby.json
   geth --networkid=4 --ipcpath="~/Library/Ethereum/rinkeby/geth.ipc" --datadir="~/Library/Ethereum/rinkeby" --cache=512 --ethstats='yournode:Respect my authoritah!@stats.rinkeby.io' --bootnodes=enode://a24ac7c5484ef4ed0c5eb2d36620ba4e4aa13b8c84684e1b4aab0cebea2ae45cb4d375b77eab56516d34bfbd3c1a833fc51296ff084b770b94fb9028c4d25ccf@52.169.42.101:30303 --rpc --rpcport 8545 --unlock 0xd96b724286c592758de7cbd72c086a8a8605417f --password ~/password.txt

   # use geth console
   geth attach ipc:/Users/user/Library/Ethereum/rinkeby/geth.ipc
   ```

* `private chain`
	- private tester chain has a default account at `0x00a329c0648769a73afac7f9381e08fb43dbea72`, loaded with lots of ether
	- you will need to create an empty password file in order to unlock the account

	```sh
	parity --dapps-hosts="all" --dapps-apis-all --jsonrpc-hosts="all" --gas-floor-target 0 --gasprice 0 --geth --chain dev --force-ui --reseal-min-period 0 --rpc  --jsonrpc-apis all --password /tmp/empty_password --unlock 0x00a329c0648769a73afac7f9381e08fb43dbea72
	```


#### Auction deployment & simulation

Deployment script can do both deployment of the auction and can also run the simulation.

Deployment:
- owner must own enough ether to deploy the contracts
- wallet is the address at which all the ETH is sent after each bid
- whitelister is the address that has permission to add/remove address to/from the auction's whitelist
- if you want to run the simulation, note the contract addresses
```sh
python -m deploy.deploy_testnet --chain privtest --owner 0x00a329c0648769a73afac7f9381e08fb43dbea72  deploy --wallet 0x00a329c0648769a73afac7f9381e08fb43dbea72 --whitelister 0x00a329c0648769a73afac7f9381e08fb43dbea72 --price-start 2000000 --price-constant 1574640000 --price-exponent 4
```

Simulation:
The bidders are given some ether at the beggining. You can use `--distribution-limit` option to cap the amount distributed.
Simulation will create n bidders that will send a random amount of ether in random intervals. If bidder runs out of funds, it will stop.
If you set `--claim-tokens` option, bidders will also try to claim the tokens at the end of the simulation.
```sh
python -m deploy.deploy_testnet --chain privtest --owner 0x00a329c0648769a73afac7f9381e08fb43dbea72 simulation --bid-interval 3 --max-bid-ceiling 0.9 --max-bid-amount 10000000000 --min-bid-amount 100000000 --bidders 100 --claim-tokens
```

Both:
To simplify things, you can just deploy & simulate:
```sh
python -m deploy.deploy_testnet --chain privtest --owner 0x00a329c0648769a73afac7f9381e08fb43dbea72  \
	deploy --price-start 2000000 --price-constant 1574640000 --price-exponent 4
	simulation --bid-interval 3 --max-bid-ceiling 0.9 --max-bid-amount 10000000000 --min-bid-amount 100000000 --bidders 100 --claim-tokens
```



#### Automatic token distribution

Deploys the Distributor contract used for claiming tokens for the bidders. Runs the script for retrieving bidder addresses from the DutchAuction contract events and batching them.

```sh
python -m distributor.main --chain privtest --auction ${AUCTION_ADDRESS} --auction-tx ${AUCTION_DEPLOY_TX_HASH}
```

Optional:

`--distributor ${DISTRIBUTOR_ADDRESS}` can be used to run the script with an already deployed Distributor contract.
`--batch-number` can be used to set how many address we send to `Distributor.distribute()`, otherwise the number is calculated with estimateGas.
`--gas-price` sets a custom gas price.

### Solidity coding style

For solidity we generally follow the style guide as shown in the [solidity documentation](http://solidity.readthedocs.io/en/develop/style-guide.html)
with a few notable exceptions:

**Variable Names**

All variable name should be in snake case, just like in python. Function names on the other hand should be mixedCase.
MixedCase is essentially like CamelCase but with the initial letter being a small letter.
This helps us to easily determine which function calls are smart contract calls in the python code side.

```js
function iDoSomething(uint awesome_argument) {
    doSomethingElse();
}
```

**Modifiers in long function declarations**


This is how the solidity documentation suggests it:

```js
function thisFunctionNameIsReallyLong(
    address x,
    address y,
    address z,
)
    public
    onlyowner
    priced
    returns (address)
{
    doSomething();
}
```

This is the minor modification we make in order to make the code more readable when quickly skimming through it.
The thinking here is to easily spot the start of the function's block when skimming and not have the modifiers
appearing as if they are a block on their own due to the hanging parentheses.

```js
function thisFunctionNameIsReallyLong(
    address x,
    address y,
    address z)

    public
    onlyowner
    priced
    returns (address)
{
    doSomething();
}
```


## Web App

Web prototype for testing auction models.


### Installation

#### Prerequisites

 * Meteor 1.5

#### Setup

```
cd app
meteor npm install
```

#### Usage

```
cd app
meteor
```
