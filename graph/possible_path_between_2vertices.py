from collections import defaultdict
def ans(u,e,n,graph,visited,pathcount):
    visited[u] = True
    if u == e:
        pathcount[0] += 1
    else:
        for k in graph[u]:
            if visited[k] == False:
                ans(k,e,n,graph,visited,pathcount)
    visited[u] = False
    

def myfun(graph,s,e,n):
    visited = [False for j in range(n+1)]
    pathcount = [0]
    ans(s,e,n,graph,visited,pathcount)
    return pathcount[0]
    

t = int(input())
while t > 0:
    graph = defaultdict(list)
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    s,e = map(int,input().split())
    for i in range(0,2*m,2):
        graph[arr[i]].append(arr[i+1])
    print(myfun(graph,s,e,n))
    t -= 1
        
    
    
    