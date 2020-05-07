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
        if i%2 == 0:
            for j in range(n):
                print(mat[i][j],end=' ')
        else:
            for j in range(n-1,-1,-1):
                print(mat[i][j],end=' ')
    print()
    t -= 1