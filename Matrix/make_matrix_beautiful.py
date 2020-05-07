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
    row = []
    col = []
    add = 0
    add1 = 0
    i = 0
    while i < n:
        for j in range(n):
            add += mat[i][j]
        row.append(add)
        add = 0 
        i += 1 
    j = 0
    while j < n:
        for k in range(n):
            add1 += mat[k][j]
        col.append(add1)
        add1 = 0
        j += 1
    r_max = max(row)
    c_max = max(col)
    t_max = max(r_max,c_max)
    ans = 0
    for i in range(n):
        ans = ans + (t_max - row[i])
    print(ans)
    t -= 1