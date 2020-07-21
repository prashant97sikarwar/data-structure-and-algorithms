def isSafe(u,v,arr,n,m,visited):
    if u >= 0 and v >= 0 and u < n and v < m and visited[u][v] == False and arr[u][v] == 'X':
        return True
    return False

def myfun(i,j,arr,n,m,visited):
    visited[i][j] = True
    row_tag = [-1,0,0,1]
    col_tag = [0,1,-1,0]
    for k in range(4):
        if isSafe(i+row_tag[k],j+col_tag[k],arr,n,m,visited):
            myfun(i+row_tag[k],j+col_tag[k],arr,n,m,visited)

def Shape(arr,n,m):
    visited = [[False for i in range(m)] for j in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == False and arr[i][j] == 'X':
                myfun(i,j,arr,n,m,visited)
                count += 1
                
    return count

if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        nm=input().split(' ')
        n=int(nm[0])
        m=int(nm[1])
        arr=input().split(' ') 
        vstd=[]
        print(Shape(arr,n,m))
            
                