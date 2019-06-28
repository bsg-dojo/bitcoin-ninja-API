import RPC_to_python_adapter as RPC

import unittest
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

RPCUSER = "admin1"
RPCPASS = "1234"
RPCPORT = 18443
myBicoindConnection = RPC.RPCbitcoin("http://%s:%s@127.0.0.1:%s"%(RPCUSER, RPCPASS, RPCPORT))


class testAddreses(unittest.TestCase):
    """
    Test different addresses
    """

    def validate_address(self, address):
        result = myBicoindConnection.validateaddress(address)['isvalid']
        return result

    def test_legacy_address(self):
        result = myBicoindConnection.getnewaddress(label = "My New Legcy Address")
        print(f"getnewaddress Legacy {result} ")

        result2 = self.validate_address(result)
        logger.debug(f"validateaddress {result2} ")
        assert result2

    def test_segwit_address(self):
        result = myBicoindConnection.getnewaddress(label = "My New Segwit Address", addressType = 'p2sh-segwit')
        print(f"getnewaddress p2sh-segwit {result} ")

        result2 = self.validate_address(result)
        logger.debug(f"validateaddress {result2} ")
        assert result2


    def test_bech32_address(self):
        result = myBicoindConnection.getnewaddress(label = "My New Segwit Address", addressType = 'bech32')
        print(f"getnewaddress bech32 {result} ")

        result2 = self.validate_address(result)
        logger.debug(f"validateaddress {result2} ")
        assert result2

if __name__ == '__main__':
    unittest.main()
