def bfs(g,N):
    visited = [False] * N
    q = []
    ans = []
    q.append(0)
    visited[0] = True
    while q:
        s = q.pop(0)
        ans.append(s)
        for i in g[s]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True
    return ans

import atexit
import io
import sys
from collections import defaultdict
import queue

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
        
        res = bfs(g.graph,N) 
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
