# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import numpy as np
# import pandas as pd
# from datetime import date
import itertools
import math
from typing import List
import networkx as nx
import matplotlib.pyplot as plt

j = range(5,101,5) # also the x axis
i = range(1,11,1)
G_connectivity = [[0 for w in range(10)]for e in range(20)]
w = 0
e = 0
sum = 0
c_q = [0 for k in j] # calculate the procentage
k = 0
for c in j:
    for n in i:
        num_of_nodes = 20
        p = 10/100
        G = nx.gnp_random_graph(num_of_nodes,p)
        if(nx.is_connected(G)==True):
            G_connectivity[w][e] = 1
            sum = sum+1
        e = e+1
    sum = (sum/10)*100
    c_q[k] = sum
    k = k+1
    sum = 0
    w = w + 1
    e = 0
# creating graph of
plt.plot(j, c_q,marker = 'o',)
# setting x and y axis range
plt.ylim(1,100)
# naming the x axis
plt.xlabel('q')
# naming the y axis
plt.ylabel('procentage')
# giving a title to my graph
plt.title('procentage of connectivity as func of q')

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
    print("the connectivity indicitor array:")
    print(G_connectivity)
    print(c_q)