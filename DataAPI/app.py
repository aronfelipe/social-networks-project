from report import Report
from data import Data

import time
class App:

    def __init__(self):
        self.report = Report()
        self.data = Data()

    def loop_on_blockchain(self):

        height = self.data.get_actual_height()

        counter_block = 0
        for n_block in range(height-10, height):
            t0 = time.time()

            block = self.data.get_block_height(n_block)
            counter_block = counter_block + 1
            counter = 0
            for transaction in block['blocks'][0]['tx']:
                counter = counter + 1
                for transaction_input in transaction['inputs']:
                    for transaction_output in transaction['out']:
                        try:
                            self.report.write_line(transaction_input['prev_out']['addr'], transaction_output['addr'], transaction['time'])
                        except Exception as e:
                            pass

                t1 = time.time()

                total = t1-t0
                if total > 60:
                    break

                # print(total)
                # print(counter)
            self.report.to_xlsx()

            print(total)

app = App()
app.loop_on_blockchain()


