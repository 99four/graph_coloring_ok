#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Damian'

import numpy as np
import random as rnd
import networkx as nx
import matplotlib.pyplot as plt
from brute import *

class Graph:
    def __init__(self, size):
        self.size = size
        self.matrix = np.zeros((size,size))

    def plot(self):
        G = nx.Graph(self.matrix)
        pos = nx.spring_layout(G) #po co to?

        labels={}
        for i in range(0,self.size):
            num = i
            labels[i] = r'$'+str(num)+'$'

        nx.draw_networkx_nodes(G, pos, node_color='y', alpha=0.7, node_size=1000) #kolejnosc nie ma znaczenia?
        nx.draw_networkx_labels(G,pos,labels,font_size=16)
        nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.9, edge_color='g')


        plt.show()


    def fill(self, saturation = 1): #domyślne nasycenie 50%
        n = self.size
        p = n * (n-1) * saturation
        self.matrix = np.zeros((n,n))
        while p > 0:
            x = rnd.randint(0, n - 1)
            y = rnd.randint(0, n - 1)

            self.matrix[x][y] = 1
            self.matrix[y][x] = 1
            p -= 1

    def return_neighbour(self, vertex):
        help_list = []
        for i,v in enumerate(self.matrix[vertex]):
            if i == vertex:
                continue
            if v == 1: #niejawna konwersja? v jest typu numpy float 64
                help_list.append(i)
        return help_list

    def check_coloring(self, coloring):
        for v in range(0,self.matrix.shape[0]):
            neighbours = self.return_neighbour(v)
            for  n in neighbours:
                if coloring[v] == coloring[n]:
                    return False
        return True

#testowe kolorowanie
graph = Graph(7)
graph.fill()

#generowanie kolorowan
brute = Brute(7,5) #graf 5 wierzcholkow, 4 kolory
colorings = brute.range()

print (graph.matrix)
print ()

for c in colorings:
    if graph.check_coloring(c):
        print('Znalazlem! ' + str(c))
        break
graph.plot()

