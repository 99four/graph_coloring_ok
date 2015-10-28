#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Damian'

import numpy as np
import random as rnd

class Graph:
    def __init__(self, size):
        self.size = size
        self.matrix = np.zeros((size,size))

    def fill(self, saturation = 0.5): #domyślne nasycenie 50%
        n = self.size
        p = n * (n-1) * saturation
        self.matrix = np.zeros((n,n))
        while p > 0:
            x = rnd.randint(0, n - 1)
            y = rnd.randint(0, n - 1)

            self.matrix[x][y] = 1
            self.matrix[y][x] = 1
            p -= 1

    
g = Graph(5)
g.fill()
print (g.matrix)
