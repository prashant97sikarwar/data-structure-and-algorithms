def issafe(x,y,graph,visited):
    global n,m
    if x >= 0 and y >= 0 and x < n and y < m and graph[x][y] == 1 and visited[x][y] == False:
        return True
    else:
        return False

def myfun(u,v,graph,visited,count):
    global n,m
    row_tag = [-1,-1,0,1,1,1,0,-1]
    col_tag = [0,1,1,1,0,-1,-1,-1]
    visited[u][v] = True
    for i in range(8):
        if issafe(u+row_tag[i],v+col_tag[i],graph,visited):
            count[0] += 1
            myfun(u+row_tag[i],v+col_tag[i],graph,visited,count)


def area(graph):
    global n,m
    visited = [[False for i in range(m)] for j in range(n)]
    result = -1
    for i in range(n):
        for j in range(m):
            if visited[i][j] == False and graph[i][j] == 1:
                count = [1]
                myfun(i,j,graph,visited,count)
                result = max(result,count[0])
    return result


t = int(input())
while t > 0:
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    c = 0
    graph = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            graph[i][j] = arr[c]
            c += 1
    print(area(graph))
    t -= 1
    