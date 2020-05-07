t = int(input())
while t > 0:
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    x = int(input())
    mat = [[0 for i in range(m)] for j in range(n)]
    c = 0
    for i in range(n):
        for j in range(m):
            mat[i][j] = arr[c]
            c += 1
    j = m-1
    i = 0
    flag = 0
    while i < n and j >= 0:
        if mat[i][j] == x:
            flag = 1
            break
        elif mat[i][j] < x:
            i += 1
        else:
            j -= 1
    if flag == 1:
        ans = 1
    else:
        ans = 0
    print(ans)
    t -= 1