import pandas as pd

class Report:

    def __init__(self):
        columns = {'sender': [], 'receiver': [], 'timestamp': []}
        self.df = pd.DataFrame(data=columns)

    def write_line(self, sender, receiver, timestamp):
        self.df = self.df.append({'sender': str(sender), 'receiver': str(receiver), 'timestamp': str(timestamp)}, ignore_index=True)

    def to_xlsx(self, block_height):
        self.df.to_excel("./NetworkBuilder/rawData/" + str(block_height) + ".xlsx")
        self.__init__()