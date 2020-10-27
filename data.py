from api import API

class Data:

    def __init__(self):
        self.api = API()

    def get_block_height(self, height):
        # TODO COLOCAR TODOS OS BLOCOS EM UMA CHAMADA.
        response = self.api.get_request('https://blockchain.info/block-height/' + str(height) + '?format=json')
        return response

    def get_transaction(self, transaction_id):
        response = self.api.get_request('https://blockchain.info/rawtx/' + str(transaction_id))
        return response

    def get_actual_height(self):
        return self.api.get_request('https://blockchain.info/latestblock')['height']
