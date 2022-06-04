import sys

# heigth, width = map(int, sys.stdin.readline().split())

import os

# instance = list(map(int, os.read(0, M).split()))

from collections import defaultdict

# nb_edges = int(input())

# g = defaultdict(dict)
# for i in range(nb_edges):
#    u, v, weight = input().split()
#    g[u][v] = int(weight)
#    # g[u][v] = int(weight)  # for an undirected graph

from random import randint
from sys import stdin

def readint():
    return int(stdin.readline())


def readarray(typ):
    return list(map(typ, stdin.readline().split()))


def readmatrix(n):
    M = []
    for _ in range(n):
        row = readarray(int)
        assert len(row) == n
        M.append(row)
        return M


def mult(M, v):
    n = len(M)  
    return [sum(M[i][j] * v[j] for j in range(n)) for i in range(n)]


def freivalds(A, B, C):
    n = len(A)
    x = [randint(0, 1000000) for j in range(n)]
    return mult(A, mult(B, x)) == mult(C, x)

if __name__ == "__main__":
    n = readint()
    A = readmatrix(n)
    B = readmatrix(n)
    C = readmatrix(n)
    print(freivalds(A, B, C))

