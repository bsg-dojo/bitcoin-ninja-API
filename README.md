# bitcoin-ninja-API
  
## Open Source Python Bitcoin library &amp; Dojo.
   
Implements the most relevant APIs: bitcoind RPCs, Bitcoin Improvement Proposals (BIPs) and helper functions in python, so you can build your bitcoin python applications. 

It also implements a REST interface of some of the same set of APIs using Flask to be able to use them for web or mobile.

### WARNING: alpha and WIP version, please ONLY use on regtest never use it on your mainnet node.
  
[![python-bitcoinrpc][python-bitcoinrpc-image]][python-bitcoinrpc-url]

[![Flask Version][flask-image]][flask-url]


## Architecture 

![Architecture](https://github.com/bsg-dojo/bitcoin-ninja-API/blob/master/architecture/190522-Architecture.png)



## MVP (Minimum Viable Prototype) 

We will start with a minimum set of methodds, BIPs, Crypto Funtions and Helpers to validate the product/market fit of the API


### 1. bitcoin RPC methods to implement in python:

Full list of [bitcoin RPC methods to adapt](https://github.com/bsg-dojo/bitcoin-ninja-API/blob/master/Methods_to_adapt.py), ( bitcoin version 0.18.0, as a referece to select methods to include on MVP)

Preliminary candidates:

####  Setup address and recieve transaction

| Caterory        | Name                     |
| --------------- | ------------------------ |
| wallet          | getnewaddress            |
| wallet          | getunconfirmedbalance    |
| wallet          | listtransactions         |
| rawtransactions | getrawtransaction        |

#### Send bitcoin transaction 

| Caterory        | Name                     |
| --------------- |------------------------- |
| wallet          | sendtoaddress            |
| wallet          | gettransaction           |
 

### 2. BIPs to Implement:

TODO

### 3. Crypto Functions to implement:

TODO

### 4. Helper functions to implement:

TODO

## 5.- bitcoin test coverage

Port the corresponding test suite of bitcoin core and create it's own set of data.

---

## Release History
* 0.0.0 TODO
    * CHANGE: MVP release

Distributed under the MIT license. See 
[License](https://github.com/bsg-dojo/bitcoin-ninja-API/blob/master/LICENSE)
for more information. 


Roberto Serrano [@StartupsPal](https://twitter.com/StarupsPal)

My time to work on this project is very limited, if you are interested on this project please consider be part of the team to contribute.

<!-- Markdown link & img dfn's -->
[flask-image]: https://img.shields.io/badge/1.0.2-Flask-green.svg 
[flask-url]: https://www.fullstackpython.com/flask.html
[python-bitcoinrpc-image]: https://img.shields.io/badge/python--bitcoinrpc-1.0-lightgrey.svg 
[python-bitcoinrpc-url]: https://github.com/jgarzik/python-bitcoinrpc

