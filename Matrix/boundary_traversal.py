t = int(input())
while t > 0:
    n1,m1 = map(int,input().split())
    arr = list(map(int,input().split()))
    mat = [[0 for i in range(m1)] for j in range(n1)]
    c = 0
    for i in range(n1):
        for j in range(m1):
            mat[i][j] = arr[c]
            c += 1
    for j in range(m1):
        print(mat[0][j],end=' ')
    for i in range(1,n1):
        print(mat[i][m1-1],end=' ')
    if n1 > 1:
        for j in range(m1-1-1,-1,-1):
            print(mat[n1-1][j],end=' ')
    if m1 > 1:
        for i in range(n1-1-1,0,-1):
            print(mat[i][0],end=' ')
    print()
    t -= 1