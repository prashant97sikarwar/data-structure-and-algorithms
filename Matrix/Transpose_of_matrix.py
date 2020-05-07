t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    mat = [[0 for i in range(n)] for j in range(n)]
    c = 0
    for i in range(n):
        for j in range(n):
            mat[i][j] = arr[c]
            c += 1
    for i in range(n):
        for j in range(i+1,n):
            mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
    for i in range(n):
        for j in range(n):
            print(mat[i][j],end=' ')
    print()
    t -= 1
            