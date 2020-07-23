def myfun(u,visited,g):
    visited[u] = True
    for j in g[u]:
        if visited[j] == False:
            myfun(j,visited,g)


def findMother(g,V):
    visited = [False] * V
    v = 0
    for i in range(V):
        if visited[i] == False:
            myfun(i,visited,g)
            v = i
    visited = [False] * V
    myfun(v,visited,g)
    for i in range(V):
        if visited[i] == False:
            return -1
    return v

import atexit
import io
import sys
from collections import defaultdict
import queue


class Graph():
    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self,u,v): 
        self.graph[u].append(v)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N,E = map(int,input().strip().split())
        g = Graph(N)
        edges = list(map(int,input().strip().split()))
        for i in range(0,len(edges),2):
            u, v = edges[i],edges[i+1]
            g.addEdge(u, v)  
        print(findMother(g.graph,N))