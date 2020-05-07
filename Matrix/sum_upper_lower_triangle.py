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
    p = 0
    for i in range(n):
        for j in range(i,n):
            p = p + mat[i][j]
    q = 0
    for i in range(n):
        for j in range(i+1):
            q = q + mat[i][j]
    print(p,end=' ')
    print(q,end=' ')
    print()
    t -= 1