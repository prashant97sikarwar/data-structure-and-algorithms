def flood(mat,x,y,prev,k):
    if x < 0 or y < 0 or x >= n or y >=m or mat[x][y] != prev or mat[x][y] == k:
        return
    mat[x][y] = k
    flood(mat,x-1,y,prev,k)
    flood(mat,x+1,y,prev,k)
    flood(mat,x,y+1,prev,k)
    flood(mat,x,y-1,prev,k)
    
def floodfill(mat,x,y,k):
    prev = mat[x][y]
    flood(mat,x,y,prev,k)
t = int(input())
while t > 0:
    n,m = map(int,input().split())
    mat = [[0 for i in range(m)] for j in range(n)]
    c = 0
    arr = list(map(int,input().split()))
    x,y,k = map(int,input().split())
    for i in range(n):
        for j in range(m):
            mat[i][j] = arr[c]
            c += 1
    floodfill(mat,x,y,k)
    for i in range(n):
        for j in range(m):
            print(mat[i][j],end=' ')
    print()
    t -= 1