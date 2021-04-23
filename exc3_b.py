# import numpy as np
# import pandas as pd
# from datetime import date
import itertools
import math
from typing import List
import networkx as nx
import matplotlib.pyplot as plt
import random

#add random edges with probability
def add_edges(G,p):
    '''
       for each node,
         add a new connection to random other node, with prob p_new_connection,
    '''
    for node in G.nodes():
        # find the other nodes this one is connected to
        connected = [to for (fr, to) in G.edges(node)]
        # and find the remainder of nodes, which are candidates for new edges
        unconnected = [n for n in G.nodes() if not n in connected]
        # probabilistically add a random edge
        if len(unconnected):  # only try if new edge is possible
            if random.random() < p:
                new = random.choice(unconnected)
                G.add_edge(node, new)
                unconnected.remove(new)
                connected.append(new)
    return


def avr_eccentricity(G):
    sum = 0
    for node in G.nodes():
       e = nx.eccentricity(G,node)
       sum = sum+e
    sum = sum/20
    return sum


j = range(5,101,5) # also the x axis
i = range(1,11,1)
x = [*j]

w = 0
e = 0
sume = 0
avr_ecc = [0 for k in j] # calculate the procentage
k = 0
for c in j:
    for n in i:
        num_of_nodes = 20
        p =x[w] /100
        #the circle graph
        G = nx.generators.classic.circulant_graph(20, [1])
        #add the rest
        add_edges(G, p)
        #compute eccentricity
        sume = sume+ avr_eccentricity(G)
        e = e+1
    sume = (sume/10)
    avr_ecc[k] = sume
    k = k+1
    sume = 0
    w = w + 1
    e = 0

print(avr_ecc)

# creating graph of
plt.plot(j, avr_ecc,marker = 'o',)

# naming the x axis
plt.xlabel('q')
# naming the y axis
plt.ylabel('avr')
# giving a title to my graph
plt.title('avr of avr eccentricity as func of q')

# function to show the plot
plt.show()

if __name__ == '__main__':
    print('write your tests here')
    print(G.size())
    print(nx.info(G))
    print("Edge set: ", G.edges())
    print("Vertex set: ", G.nodes())
    nx.draw(G)
    plt.show()

