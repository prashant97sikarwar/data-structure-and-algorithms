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
    for i in range(n1-1,-1,-1):
        for j in range(m1):
            print(mat[i][j],end=' ')
    print()
    t = int(t)
    t -= 1