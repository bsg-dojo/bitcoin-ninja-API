# bitcoin-ninja-API
  
## Open Source Bitcoin library &amp; Dojo.
   
Implements the most relevant APIis, Bitcoin Improvement Proposals (BIPs) and helper functions. 
So you can build your application on top of it.

[![Flask Version][flask-image]][flask-url]


## Architecture 

![Architecture]()


Full list of [bitcoin RPC methods to implement](https://github.com/bsg-dojo/bitcoin-ninja-API/blob/master/RPCMethodstoImplement.py).

## MVP (Minimum Viable Prototype) 

### methods / function helpers to implement MVP:


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
port of the test suite of bitcoin core with their own data.

---

For more examples and usage, please refer to the [Wiki](https://github.com/bsg-dojo/bitcoin-ninja-API/blob/master/RPCMethodstoImplement.py).

## Development setup

Describe how to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

## Release History


* 0.1.0
    * CHANGE: Update docs (module code remains unchanged)
* 0.2.0
    * CHANGE: Remove `setDefaultXYZ()`
    * ADD: Add `init()`


Distributed under the MIT license. See 
[License](https://github.com/bsg-dojo/bitcoin-ninja-API/blob/master/LICENSE)
for more information. 


Roberto Serrano [@StartupsPal](https://twitter.com/StarupsPal)

## Contributing

1. Fork it (git clone <https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[flask-image]: https://img.shields.io/badge/1.0.2-Flask-green.svg 
[flask-url]: https://www.fullstackpython.com/flask.html
 
