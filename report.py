import pandas as pd

class Report:

    def __init__(self):
        columns = {'sender': [], 'receiver': [], 'timestamp': []}
        self.df = pd.DataFrame(data=columns)

    def write_line(self, sender, receiver, timestamp):
        self.df = self.df.append({'sender': str(sender), 'receiver': str(receiver), 'timestamp': str(timestamp)}, ignore_index=True)

    def to_xlsx(self):
        self.df.to_excel("transation.xlsx")

# report = Report()

# report.write_line("teste", "teste", "teste")
        
# print(report.df)

# report.to_xlsx()