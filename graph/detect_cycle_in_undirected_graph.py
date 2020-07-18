def solve(v,visited,parent,g):
    visited[v] = True
    for j in g[v]:
        if visited[j] == False:
            if solve(j,visited,v,g) == True:
                return True
        elif parent != j:
            return True
    return False

def isCyclic(g,n):
    visited = [False for i in range(n)]
    for i in range(n):
        if visited[i] == False:
            if solve(i,visited,-1,g) == True:
                return 1
    return 0

import atexit
import io
import sys
from collections import defaultdict

class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self,u,v): 
        self.graph[u].append(v)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N,E = map(int,input().strip().split())
        g = Graph(N)
        edges = list(map(int,input().strip().split()))

        for i in range(0,len(edges),2):
            u,v = edges[i],edges[i+1]
            g.addEdge(u,v) 
            g.addEdge(v,u)
        print(isCyclic(g.graph,N))