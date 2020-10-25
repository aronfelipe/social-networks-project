from report import Report
from data import Data

import time
class App:

    def __init__(self):
        self.report = Report()
        self.data = Data()

    def loop_on_blockchain(self):

        t0 = time.time()

        height = self.data.get_actual_height()

        block = self.data.get_block_height(height, 1)
        
        counter = 0
        for transaction in block['blocks'][0]['tx']:
            counter = counter + 1
            # transaction = self.data.get_transaction(transaction_id)

            for transaction_input in transaction['inputs']:
                for transaction_output in transaction['out']:
                    # print("---------------------------------------------------")
                    # print(transaction_input)
                    # print(transaction_output)
                    # print(transaction)
                    try:
                        # print(transaction_input['prev_out']['addr'])
                        # print(transaction_output['addr'])
                        self.report.write_line(transaction_input['prev_out']['addr'], transaction_output['addr'], transaction['time'])
                        # print(self.report.df)
                    except Exception as e:
                        print(e)
                        
                        pass

        t1 = time.time()
        self.report.to_xlsx()

        total = t1-t0
        print(total)
        print(counter)
            # if counter >= 10:
            #     self.report.to_xlsx()
            #     break

        # transaction_count = len(block['txids'])

        # while len(block['txids']) == 500:

        #     block = self.data.get_block_height(height, transaction_count)

        #     for transaction_id in block['txids']:
        #         transaction = self.data.get_transaction(transaction_id)

        #         for transaction_input in transaction['inputs']:
        #             for transaction_output in transaction['out']:
        #                 try:
        #                     self.report.write_line(transaction_input['addr'], transaction_output['addr'], transaction['confirmed'])
        #                 except:
        #                     pass
        #         print(self.report.df)
            
        #     transaction_count + len(block['txids'])

app = App()
app.loop_on_blockchain()


