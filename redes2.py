import os
import pandas as pd
import networkx as nx
import freeman as fm
import time

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


t1 = time.time()
centralidades = {}
#networks = os.listdir('./NetworkBuilder/network/')
g = fm.load('./NetworkBuilder/network/655366.gml')
BETWEENNESS_CENTRALITY = nx.betweenness_centrality(g)
centralidades['655366'] = getCentralization(BETWEENNESS_CENTRALITY, "between")


data = {'Block': centralidades.keys(), 'Centralidade': centralidades.values()}
volDf = pd.DataFrame.from_dict(data)
volDf.to_excel("centralidade2.xlsx")
t2 = time.time()

tf = t2 - t1

print(tf)


