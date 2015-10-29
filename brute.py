#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Damian'

#klasa generujaca kolorowania dla c(bound) kolorow i e(digits) wierzcholkow
class Brute:
    def __init__(self, digits, bound):
        self.digits = digits
        self.bound = bound

    def first(self):
        return [0] * self.digits

    def increment(self, num, pos = -1):
        following = num[:] #plytka kopia, zmienic nazwe zmiennej following
        following[pos] += 1

        if following[pos] == self.bound:
            following[pos] = 0
            return self.increment(following, pos-1) #dlaczego musi byc return?
        return following

    def range(self):
        numbers = [self.first()]
        for i in range(1,self.bound**self.digits):
            numbers.append(self.increment(numbers[-1]))
        return numbers
