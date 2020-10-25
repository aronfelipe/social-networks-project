import pandas as pd

def create_nodes(df):
    allWallets = []
    allWallets = df['sender'] + df['receiver']
    
    allWallets = list(set(allWallets))

    return allWallets


def main():
    df = pd.read_excel('transation.xlsx')
    nodes = create_nodes(df)

    with open("./network.gml", "w") as f:
        f.write('graph [\n')
        f.write('  directed 1\n')

        for i in range(len(nodes)):
            f.write('  node [\n')
            f.write('    id {}\n'.format(i))
            f.write('    name "{}"\n'.format(nodes[i]))
            f.write('  ]\n')
        
        for index, row in df.iterrows():
            f.write('  edge [\n')
            f.write('    source {}\n'.format(row['sender']))
            f.write('    target {}\n'.format(row['receiver']))
            f.write('  ]\n')

        f.write(']\n')

main()
#create_nodes()