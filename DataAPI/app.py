from report import Report
from data import Data
import time
import numpy as np
import requests


class App:

    def __init__(self):
        self.report = Report()
        self.data = Data()

    def generate_volatility(self, timestamp):
        response = requests.get("https://min-api.cryptocompare.com/data/v2/histominute?fsym=BTC&tsym=USD&limit=10&toTs=" + str(timestamp))
        data = response.json()["Data"]["Data"]

        minute_list = []

        for i in range(len(data)):
            minute_list.append(response.json()["Data"]["Data"][i]['close'])
        
        volatility_10_minutes = np.std(minute_list, ddof = 1)
        
        self.report.write_line(volatility_10_minutes, volatility_10_minutes, timestamp)
        
    def loop_on_blockchain(self, initial_height, final_height):

        counter_block = 0
        for n_block in range(initial_height, final_height):
            t0 = time.time()
            block = self.data.get_block_height(n_block)
            self.generate_volatility(block['blocks'][0]['time'])
            counter_block = counter_block + 1
            counter = 0
            for transaction in block['blocks'][0]['tx']:
                counter = counter + 1
                for transaction_input in transaction['inputs']:
                    for transaction_output in transaction['out']:
                        try:
                            self.report.write_line(transaction_input['prev_out']['addr'], transaction_output['addr'], transaction['time'])
                            t1 = time.time()
                            total = t1-t0
                            if total > 60:
                                break
                        except:
                            t1 = time.time()
                            total = t1-t0
                            if total > 60:
                                break
                            
                    t1 = time.time()
                    total = t1-t0
                    if total > 60:
                        break

                t1 = time.time()
                total = t1-t0
                if total > 60:
                    break

            self.report.to_xlsx(n_block)

app = App()
# app.loop_on_blockchain(657584, 657581+14)
# app.loop_on_blockchain(657581+14, 657581+28)
# app.loop_on_blockchain(657581+28, 657581+42)
# app.loop_on_blockchain(657581+42, 657581+56)
# app.loop_on_blockchain(657581+56, 657581+70)
# app.loop_on_blockchain(657581+70, 657581+84)
# app.loop_on_blockchain(657581+84, 657581+98)
# app.loop_on_blockchain(657581+98, 657581+112)
# app.loop_on_blockchain(657581+112, 657581+126)
# app.loop_on_blockchain(657581+126, 657581+140)
# app.loop_on_blockchain(657581+140, 657581+154)

app.loop_on_blockchain(657699, 657700)
