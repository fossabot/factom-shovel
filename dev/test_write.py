import time
import uuid
import unittest
import factom 

BLKTIME = 15  # sec


class TestSim(unittest.TestCase):
    """ Verify APIs of Factomd sim and wallet run properly """


    def setUp(self):
        """ open client connections """
        self.w = factom.FactomWalletd()
        self.f = factom.Factomd(
            host='http://127.0.0.1:8088',
            fct_address='FA2jK2HcLnRdS94dEcU27rF3meoJfpUcZPSinpb7AwQvPRY6RL1Q',
            ec_address='EC3Hu1W7uMHf7CtSva1cMyr5rXKsu7rVqQtkJCDHqEV9dgh5FjAj'
            # username='rpc_username',
            # password='rpc_password'
        )

    def tearDown(self):
        """ close client connections """
        self.w.session.close()
        self.f.session.close()

    def test_buy_ec(self):
        """ test buying entry credits """
        
        # use a funded coinbase address with a known secret key
        self.w.import_address("Fs3E9gV6DXsYzf7Fqx1fVBQPQXV695eP3k5XbmHEZVRLkMdD9qCK")
        self.w.import_address("Es3C7Ybmj8qoG1xZNrTm18EWKjW3BgvXQDFWZ1q1LvxxUBW5S5DL")

        r = self.f.entry_credit_rate()
        rate = r['rate']
        self.assertEqual(rate, 1000)
        print(r)

        r = self.f.factoid_balance(self.f.fct_address)
        print(r)

        r = self.w.fct_to_ec(self.f, 50 * rate, fct_address=self.f.fct_address, ec_address=self.f.ec_address)
        self.assertEqual(r['message'], 'Successfully submitted the transaction')

        ident = uuid.uuid4()
        r = self.w.new_chain(self.f, [ident.bytes, b'chain', b'id'], b'chain_content', ec_address=self.f.ec_address)
        print(r)


if __name__ == '__main__':
    unittest.main()
