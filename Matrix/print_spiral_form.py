t = int(input())
while t > 0:
    m,n = map(int,input().split())
    arr = list(map(int,input().split()))
    mat = [[0 for i in range(n)] for j in range(m)]
    c = 0
    for i in range(m):
        for j in range(n):
            mat[i][j] = arr[c]
            c += 1
    k = 0
    l = 0
    while k < m and l < n:
        for i in range(l,n):
            print(mat[k][i],end=' ')
        k += 1
        for i in range(k,m):
            print(mat[i][n-1],end=' ')
        n -= 1
        if k < m:
            for i in range(n-1,(l-1),-1):
                print(mat[m-1][i],end=' ')
            m -= 1
        if l < n:
            for i in range(m-1,(k-1),-1):
                print(mat[i][l],end=' ')
            l += 1 
    print()
    t -= 1