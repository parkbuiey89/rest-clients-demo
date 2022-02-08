from web3 import Web3

class Sanity_check:
    wallet_list = []

    def __init__(self):
        self.connection_check = self.connection_check()
        #self.results = self.results()

    def connection_check(self):
        w3 = Web3(Web3.HTTPProvider("https://withered-ancient-forest.quiknode.pro/833ecd82b96ad1b99b9bbbf9fac2afee136959b8/"))
        f = open('new_block.json', 'w')
        block_identifer = w3.eth.get_block('latest')
        transactions = web3.eth.get_block_transaction_count(block_identifier)
        for item in new_query_set:
            f.write(item + "\n")
        f.close()

    def results(self):
        if self.connection_check:
            print("tru dog")
        else:
            print("no foo")

s = Sanity_check()

