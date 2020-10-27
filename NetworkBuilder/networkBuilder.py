import pandas as pd
import numpy as np


def create_nodes(df):
    allWallets = []

    allWallets = list(df['sender']) + list(df['receiver'])
    
    allWallets = list(set(allWallets))

    return allWallets


def main():
    df = pd.read_excel('transation.xlsx')
    listaDf = np.array_split(df, 10)
    counter = 0
    for df in listaDf:
        counter += 1
        df = df.drop_duplicates(subset=['sender', 'receiver'], keep=False)

        nodes = create_nodes(df)
        node_dict = {}

        with open("./network"+str(counter)+".gml", "w") as f:
            f.write('graph [\n')
            f.write('  directed 1\n')

            for i in range(len(nodes)):
                f.write('  node [\n')
                f.write('    id {}\n'.format(i))
                f.write('    name "{}"\n'.format(nodes[i]))
                f.write('  ]\n')
                node_dict[nodes[i]] = i
            
            for index, row in df.iterrows():
                if(row['sender'] != row['receiver']):
                    f.write('  edge [\n')
                    f.write('    source {}\n'.format(node_dict[row['sender']]))
                    f.write('    target {}\n'.format(node_dict[row['receiver']]))
                    f.write('  ]\n')

            f.write(']\n')

main()