def solve(v,graph,n,st,visited):
    visited[v] = True
    st[v] = True
    for j in graph[v]:
        if visited[j] == False:
            if solve(j,graph,n,st,visited) == True:
                return True
        elif st[j] == True:
            return True 
    st[v] = False
    return False
    
    
def isCyclic(n, graph):
    visited = [False for i in range(n)]
    st = [False] * n
    for i in range(n):
        if visited[i] == False:
            if solve(i,graph,n,st,visited) == True:
                return 1
    return 0

from collections import defaultdict

def creategraph(n, arr, graph):
    i = 0
    while i < 2 * e:
        graph[arr[i]].append(arr[i + 1])
        i += 2

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n,e = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, arr, graph)
        if isCyclic(n, graph):
            print(1)
        else:
            print(0)