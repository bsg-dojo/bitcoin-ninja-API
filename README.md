# bitcoin-ninja-API
  
## Open Source Python Bitcoin library &amp; Dojo.
   
Implements the most relevant APIs: bitcoind RPCs, Bitcoin Improvement Proposals (BIPs) and helper functions in python, so you can build your python application. 

It also implements a REST interface of the same set of APIs using Flask to be able to use them for web or mobile.

[![python-bitcoinrpc][python-bitcoinrpc-image]][python-bitcoinrpc-url]

[![Flask Version][flask-image]][flask-url]


## Architecture 

![Architecture](https://github.com/bsg-dojo/bitcoin-ninja-API/blob/master/architecture/190522-Architecture.png)


Full list of [bitcoin RPC methods to adapt](https://github.com/bsg-dojo/bitcoin-ninja-API/blob/master/RPCMethodstoImplement.py), Work in Progress.


## MVP (Minimum Viable Prototype) 

### MVP methods / function helpers to implement in python:


#### 1.- Setup address and recieve transaction

| Caterory        | Name                     |
| --------------- | ------------------------ |
| wallet          | getnewaddress            |
| wallet          | getunconfirmedbalance    |
| wallet          | listtransactions         |
| rawtransactions | getrawtransaction        |

#### 2.- Send bitcoin transaction 

| Caterory        | Name                     |
| --------------- |------------------------- |
| wallet          | sendtoaddress            |
| wallet          | gettransaction           |
 

#### 3.- bitcoin test coverage
Port the corresponding test suite of bitcoin core with it's own data.

---

## Release History
* 0.0.0 TODO
    * CHANGE: MVP release

Distributed under the MIT license. See 
[License](https://github.com/bsg-dojo/bitcoin-ninja-API/blob/master/LICENSE)
for more information. 


Roberto Serrano [@StartupsPal](https://twitter.com/StarupsPal)

<!-- Markdown link & img dfn's -->
[flask-image]: https://img.shields.io/badge/1.0.2-Flask-green.svg 
[flask-url]: https://www.fullstackpython.com/flask.html
[python-bitcoinrpc-image]: https://img.shields.io/badge/python--bitcoinrpc-1.0-lightgrey.svg 
[python-bitcoinrpc-url]: https://github.com/jgarzik/python-bitcoinrpc

