#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Damian'

class Brute:
    def __init__(self, digits, bound):
        self.digits = digits
        self.bound = bound

    def first(self):
        return [0] * self.digits

    def increment(self, num, pos = -1):

        num[pos] += 1

        if num[pos] == self.bound:
            num[pos] = 0
            self.increment(num, pos-1)

        print (num)

g = Brute(5,5)

nums = g.first()

for i in range(1,g.digits**g.bound):
    g.increment(nums)

print (i)
