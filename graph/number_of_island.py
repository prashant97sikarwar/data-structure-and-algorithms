import sys
sys.setrecursionlimit(100000)
def issafe(i,j,visited,N,M,A):
    if i >= 0 and j >= 0 and i < N and j < M:
        if visited[i][j] == False and A[i][j] == 1:
            return True
    return False

def dfs(i,j,visited,N,M,A):
    row_tag = [-1,-1,-1,0,1,1,1,0]
    col_tag = [-1,0,1,1,1,0,-1,-1]
    visited[i][j] = True
    
    for k in range(8):
        if issafe(i+row_tag[k],j+col_tag[k],visited,N,M,A):
            dfs(i+row_tag[k],j+col_tag[k],visited,N,M,A)
    


def findIslands(A, N, M):
    visited = [[False for i in range(M)] for j in range(N)]
    count = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == False and A[i][j] == 1:
                dfs(i,j,visited,N,M,A)
                count += 1
    return count

t=int(input())
for cases in range(t):
    n,m = map(int,input().strip().split())
    cell_info = list(map(int,input().strip().split()))
    a = []
    k = 0 
    for i in range(n):
        row_i = []
        for j in range(m):
            row_i.append(cell_info[k])
            k+=1
        a.append(row_i)
    print(findIslands(a,n,m))