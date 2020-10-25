from api import API

class Data:

    def __init__(self):
        self.api = API()

    def get_block_height(self, height, start):
        # return self.api.get_request('https://api.blockcypher.com/v1/btc/main/blocks/' + str(height) + '?txstart=' + str(start) + '&limit=500')
        request = self.api.get_request('https://blockchain.info/block-height/654276?format=json')
        # print(request)
        return request

    def get_transaction(self, transaction_id):
        request = self.api.get_request('https://blockchain.info/rawtx/' + str(transaction_id))
        # print(request)
        return request

    def get_actual_height(self):
        return self.api.get_request('https://blockchain.info/latestblock')['height']
