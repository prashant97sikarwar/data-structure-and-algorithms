import queue

def ans(graph,n,x):
    visited = [False for i in range(n)]
    level = [None] * n
    que = queue.Queue()
    que.put(0)
    level[0] = 0
    visited[0] = True
    
    while (not que.empty()):
        p = que.get()
        for j in graph[p]:
            if visited[j] == False:
                que.put(j)
                visited[j] = True
                level[j] = level[p] + 1
                if j == x:
                    return level[j]
    return -1

from collections import defaultdict
t = int(input())
while t > 0:
    graph = defaultdict(list)
    n,e = map(int,input().split())
    for i in range(e):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    x =  int(input())
    print(ans(graph,n,x))
    t -= 1
    