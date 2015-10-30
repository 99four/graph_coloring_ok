#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Damian'

from graph import *

class Greedy:
    def __init__(self):
        self.coloring = [None] * 5

    def first(self):
        self.coloring[0] = 0
