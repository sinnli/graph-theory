# import numpy as np
# import pandas as pd
# from datetime import date
import itertools
import math
from typing import List
import networkx as nx
import matplotlib.pyplot as plt


j = range(5,101,5) # also the x axis
#the x axcis

t3_n = [0 for e in j]
t3_n.append(0)
t3_n.append(0)
x = [*j]
x.append(150)
x.append(200)
print(x)
w = 0
e = 0
k = 0
sumi  = 0

for c in j:
    for n in range(1,11,1):
        num_of_nodes = x[w] #num of verticles is n(the range of j)
        p = 1/2
        G = nx.gnp_random_graph(num_of_nodes,p)
        number_of_triangles = sum(nx.triangles(G).values()) / 3
        sumi = sumi+number_of_triangles
        e = e + 1
    sumi = (sumi/ 10)
    t3_n[k] = sumi
    k = k + 1
    sumi = 0
    w = w + 1
    e = 0
#add n = 150
w = len(x)-2
e = 0
sumi  = 0
for n in range(1, 11, 1):
    num_of_nodes = x[w]  # num of verticles is n(the range of j)
    p = 1 / 2
    G = nx.gnp_random_graph(num_of_nodes, p)
    number_of_triangles = sum(nx.triangles(G).values()) / 3
    sumi = sumi + number_of_triangles
    e = e + 1
sumi = (sumi / 10)
t3_n[w] = sumi

#add n = 200
w = len(x)-1
e = 0
sumi  = 0
for n in range(1, 11, 1):
    num_of_nodes = x[w]  # num of verticles is n(the range of j)
    p = 1 / 2
    G = nx.gnp_random_graph(num_of_nodes, p)
    number_of_triangles = sum(nx.triangles(G).values()) / 3
    sumi = sumi + number_of_triangles
    e = e + 1
sumi = (sumi / 10)
t3_n[w] = sumi
print(sumi)

print(t3_n)


# creating graph of
plt.plot(x, t3_n,marker = 'o',)

# naming the x axis
plt.xlabel('num of verticles (n)')
# naming the y axis
plt.ylabel('avr')
# giving a title to my graph
plt.title('avr of num of triagngles as func of n (verticles)')

# function to show the plot
plt.show()

if __name__ == '__main__':
    print('write your tests here')
"""
    print(G.size())
    print(nx.info(G))
    print("Edge set: ", G.edges())
    print("Vertex set: ", G.nodes())
    nx.draw(G)
    plt.show()
"""