import math

def mindis(dist,sptset,v,g):
    mn = math.inf
    for x in range(v):
        if dist[x] < mn and sptset[x] == False:
            mn = dist[x]
            min_ind = x
    return min_ind
        


def dijkstra(src, V, g):
    dist = [math.inf] * V
    dist[src] = 0
    sptset = [False] * V
    for vt in range(V):
        u = mindis(dist,sptset,V,g)
        sptset[u] = True
        for j in range(V):
            if g[u][j] > 0 and sptset[j] == False and dist[j] > dist[u] + g[u][j]:
                dist[j] = dist[u]  + g[u][j]
    return dist

def printSolution(dist, V):
    for node in range(V):
        print(dist[node] , end=' ')
    print()


if __name__ == '__main__':
    t = int(input())
    for tst in range(t):
        v = int(input())
        graph = [[0 for column in range(v)]
                    for row in range(v)]

        lst = [int(x) for x in input().strip().split()]
        k=0
        for i in range(v):
            for j in range(v):
                graph[i][j] = lst[k]
                k+=1
        s = int(input())
        res = dijkstra(s, v, graph)
        
        printSolution (res, v)