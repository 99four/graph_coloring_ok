#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Damian'

import numpy as np
import random as rnd
import networkx as nx
import matplotlib.pyplot as plt
from brute import *

color_scheme = ['red', 'green', 'blue', 'yellow', 'darkviolet', 'orange', 'grey', 'aqua', 'olive']

class Graph:
    def __init__(self, size):
        self.size = size
        self.matrix = np.zeros((size,size))

    def plot(self, coloring=None):
        G = nx.Graph(self.matrix)
        pos = nx.spring_layout(G) #po co to?

        labels={}
        for i in range(0,self.size):
            num = i
            labels[i] = r'$'+str(num)+'$'

        #obsluga kolorow
        if coloring is None:
            colors_to_use = self.coloring
        else:
            colors_to_use = coloring

        color_list = []
        for x in colors_to_use:
            color_list.append(color_scheme[x])

        nx.draw_networkx_nodes(G, pos, node_color=color_list, alpha=0.7, node_size=1000) #kolejnosc nie ma znaczenia?
        nx.draw_networkx_labels(G,pos,labels,font_size=16)
        nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.9, edge_color='g')

        plt.show()


    def fill(self, saturation = 0.6): #domyślne nasycenie 50%
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
        self.coloring = coloring
        return True

v = 5 #liczba wierzcholkow

graph = Graph(v)
graph.fill()

def bruteForceAlgo():
    found_solution = False
    for i in range(0,v+1):
        if found_solution: break
        b = Brute(v,i)
        colorings = b.range()
        for c in colorings:
            if graph.check_coloring(c):
                print('Znalazlem! ' + str(c) + ' liczba chromatyczna grafu wynosi ' + str(i))
                found_solution = True
                break

bfs_result = []
queue = []


def bfs(start):
    bfs_result.append(start)
    neighbours = graph.return_neighbour(start)
    for n in neighbours:
        bfs_result.append(n)
        queue.append(n)
    #print ('poczatek neighbours: ' + str(neighbours))
    #print ('poczatek queue: ' + str(queue) + '\n')

    while queue:
        neighbours = graph.return_neighbour(queue[0])
        #print ('kolejka: ' + str(queue))
        #print ('sasiedzi wierzcholka : ' + str(queue[0]) + ': ' + str(neighbours))
        del queue[0]
        for n in neighbours:
            if n not in bfs_result:
                #print ('dodalem rozwiazanie ' + str(n))
                bfs_result.append(n)
                queue.append(n)

bfs(0)
print ('wynik bfs to: ' + str(bfs_result))
print (len(bfs_result))

coloring = [-1] * v
def greedyColoring():
    coloring[bfs_result[0]] = 0

    for i in range(1,len(bfs_result)):
        neighbours = graph.return_neighbour(bfs_result[i])

        neigh_colorings = []
        for k in neighbours:
            neigh_colorings.append(coloring[k])
        max_neigh_color = max(neigh_colorings)
        print (max_neigh_color)
        neigh_colorings.clear()

        coloring[bfs_result[i]] = max_neigh_color + 1
    print (coloring)


greedyColoring()
#bruteForceAlgo()
graph.plot(coloring)
