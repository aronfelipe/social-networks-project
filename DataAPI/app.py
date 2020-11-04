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
        # print(volatility_10_minutes)
        
        self.report.write_line(volatility_10_minutes, volatility_10_minutes, timestamp)
        
    def loop_on_blockchain(self, initial_height, final_height):

        block = self.data.get_block_height(initial_height)

        self.generate_volatility(block['blocks'][0]['time'])

        counter_block = 0
        for n_block in range(initial_height, final_height):
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
                            # print(e)
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
# app.loop_on_blockchain(655275, 655289)
app.loop_on_blockchain(655300, 655303)
# app.loop_on_blockchain(655303, 655317)
# app.loop_on_blockchain(655317, 655331)
# app.loop_on_blockchain(655331, 655345)
# app.loop_on_blockchain(655345, 655359)
# app.loop_on_blockchain(655359, 655373)
# app.loop_on_blockchain(655373, 655387)
# app.loop_on_blockchain(655387, 655401)
# app.loop_on_blockchain(655401, 655419)

# print(60 * 14)
# print(840 / 60 / 24)

# import numpy as np

# calculo = (655404 - 651318)

# print(calculo)

# print()

# lista = np.arange(651318, 655404, 681)

# print((681 * 60) / 60 / 24)

# print(144*60)

# print(8640/60/24)
