def fun(v,visited,st,n,adj):
    visited[v] = True
    for j in adj[v]:
        if visited[j] == False:
            fun(j,visited,st,n,adj)
    st.insert(0,v)
        


def topoSort(n, adj):
    visited = [False for i in range(n)]
    st = []
    for i in range(n):
        if visited[i] == False:
            fun(i,visited,st,n,adj)
    return st
    
    
def creategraph(e, n, arr, graph):
    i = 0
    while i<2*e:
        graph[arr[i]].append(arr[i+1])
        i+=2

from collections import defaultdict
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, N, arr, graph)
        res = topoSort(N, graph)
        # print res
        valid=True
        for i in range(N):
            n = len(graph[res[i]])
            for j in range(len(graph[res[i]])):
                for k in range(i+1, N):
                    if res[k]==graph[res[i]][j]:
                        n-=1
            if n!=0:
                valid=False
                break
        if valid:
            print(1)
        else:
            print(0)