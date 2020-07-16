def dfs_recursive(arr,g, key,visited):
    if visited[key] == False:
        visited[key] = True
        arr.append(key)
        for new_key in g[key]:
            dfs_recursive(arr,g, new_key,visited)
    return arr
def dfs(g,N):
    visited = [False] * N
    arr = []
    return dfs_recursive(arr,g, 0,visited)

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
