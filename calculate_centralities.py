import os
import pandas as pd
import networkx as nx
import freeman as fm
import numpy as np
import time 
import math

from NetworkBuilder.networkBuilder import *
from DataAPI.app import *

print("Começou o processamento", flush=True)

def getCentralization(centrality, c_type):

    c_denominator = float(1)

    n_val = float(len(centrality))

    print(str(len(centrality)) + "," +  c_type + "\n")

    if (c_type=="degree"):
        c_denominator = (n_val-1)*(n_val-2)

    if (c_type=="close"):
        c_top = (n_val-1)*(n_val-2)
        c_bottom = (2*n_val)-3	
        c_denominator = float(c_top/c_bottom)

    if (c_type=="between"):
        c_denominator = (n_val*n_val*(n_val-2))

    if (c_type=="eigen"):

        '''
        M = nx.to_scipy_sparse_matrix(G, nodelist=G.nodes(),weight='weight',dtype=float)
        eigenvalue, eigenvector = linalg.eigs(M.T, k=1, which='LR') 
        largest = eigenvector.flatten().real
        norm = sp.sign(largest.sum())*sp.linalg.norm(largest)
        centrality = dict(zip(G,map(float,largest)))
        '''

        c_denominator = sqrt(2)/2 * (n_val - 2)
        
        
        

    #start calculations	

    c_node_max = max(centrality.values())


    c_sorted = sorted(centrality.values(),reverse=True)
    


    print ("max node" + str(c_node_max) + "\n")

    c_numerator = 0

    for value in c_sorted:

        if c_type == "degree":
            #remove normalisation for each value
            c_numerator += (c_node_max*(n_val-1) - value*(n_val-1))
        else:
            c_numerator += (c_node_max - value)

    print ('numerator:' + str(c_numerator)  + "\n")	
    print ('denominator:' + str(c_denominator)  + "\n")	

    network_centrality = float(c_numerator/c_denominator)

    if c_type == "between":
        network_centrality = network_centrality * 2

    return network_centrality

def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out

app = App()

block_init = 657355

app.loop_on_blockchain(block_init, block_init+864)
# app.loop_on_blockchain(block_init+14, block_init+28)
# app.loop_on_blockchain(block_init+28, block_init+42)
# app.loop_on_blockchain(block_init+42, block_init+56)
# app.loop_on_blockchain(block_init+56, block_init+70)
# app.loop_on_blockchain(block_init+70, block_init+84)
# app.loop_on_blockchain(block_init+84, block_init+98)
# app.loop_on_blockchain(block_init+98, block_init+112)
# app.loop_on_blockchain(block_init+112, block_init+126)
# app.loop_on_blockchain(block_init+126, block_init+140)

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

files = os.listdir('./NetworkBuilder/rawData')

create_vol(files)

networks = os.listdir('./NetworkBuilder/network/')

print(len(networks))

chunk = chunkIt(networks, 16)

chunk = np.array_split(networks, 16)

for i in range(0, 16):
    print(i)
    centralidades = {}

    for rede in range(0, len(chunk[i])):
        print(rede)
        print(chunk[i][rede])
        print(len(chunk[rede]))
        t1 = time.time()
        g = fm.load('./NetworkBuilder/network/' + chunk[i][rede])
        BETWEENNESS_CENTRALITY = nx.betweenness_centrality(g)
        centralidades[chunk[i][rede][:-4]] = getCentralization(BETWEENNESS_CENTRALITY, "between")
        t2 = time.time()
        tf = t2 - t1
        print(tf, flush=True)
        print(centralidades)
    
    print(centralidades)

    data = {'Block': centralidades.keys(), 'Centralidade': centralidades.values()}
    volDf = pd.DataFrame.from_dict(data)
    volDf.to_excel("centralidade" + str(i) + ".xlsx")
