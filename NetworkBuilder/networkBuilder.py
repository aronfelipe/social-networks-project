import pandas as pd
import numpy as np
import os
from multiprocessing import Process





def paralel(n):
    files = os.listdir('./rawData')
    avg = len(files) / float(n)
    out = []
    last = 0.0

    while last < len(files):
        out.append(files[int(last):int(last + avg)])
        last += avg

    return out




def create_dfs(list_files):
    dfs = []
    vol_dict = {}
    for f in list_files:
        try:
            df = pd.read_excel("./rawData/"+f)
            vol = df["sender"][0]
            vol_dict[f[:-5]] = vol
            df.drop([0])
            df = df.drop_duplicates(subset=['sender', 'receiver'], keep=False)

            nodes = create_nodes(df)
            node_dict = {}

            with open("./network/"+f[:-5]+".gml", "w") as f:
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
        except:
            print(f)

    data = {'Block': vol_dict.keys(), 'Volatilidade': vol_dict.values()}
    volDf = pd.DataFrame.from_dict(data)
    volDf.to_excel("vol_df.xlsx")
    return dfs




def create_nodes(df):
    allWallets = []

    allWallets = list(df['sender']) + list(df['receiver'])
    
    allWallets = list(set(allWallets))

    return allWallets


def create_network(name, df):
    #df = pd.read_excel('transation.xlsx')
    listaDf = np.array_split(df, 10)
    counter = 0
    for df in listaDf:
        counter += 1
        df = df.drop_duplicates(subset=['sender', 'receiver'], keep=False)

        nodes = create_nodes(df)
        node_dict = {}

        with open("./network/"+str(counter)+".gml", "w") as f:
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



#df = pd.read_excel("./rawData/655390.xlsx")
#print(df)

#df = df["sender"][0]


#s = "655390.xlsx"
#print(s[:-5])
if __name__ == "__main__":
    files = paralel(5)
    print(files)
    process = []

    p1 = Process(target=create_dfs(files[0]))
    process.append(p1)
    p1.start()

    p2 = Process(target=create_dfs(files[1]))
    process.append(p2)
    p2.start()

    p3 = Process(target=create_dfs(files[2]))
    process.append(p3)
    p3.start()

    p4 = Process(target=create_dfs(files[3]))
    process.append(p4)
    p4.start()

    p5 = Process(target=create_dfs(files[4]))
    process.append(p5)
    p5.start()


    for p in process:
        p.join()
    
