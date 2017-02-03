# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time

def primes():
    n = int(input("How many primes should I go up to?"))
    start_time = time.clock()
    out = list()
    X = [True] * (n+1)
    for p in range(2, n+1):
        if (X[p]):
            out.append(p)
            for i in range(p, n+1, p):
                X[i] = False
    print(out)
    print(round((time.clock() - start_time), 4), "seconds")
