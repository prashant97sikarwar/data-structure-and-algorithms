t = int(input())
while t > 0:
    n1,m1 = map(int,input().split())
    arr1 = list(map(int,input().split()))
    n2,m2 = map(int,input().split())
    arr2 = list(map(int,input().split()))
    mat1 = [[0 for i in range(m1)] for j in range(n1)]
    mat2 = [[0 for i in range(m2)] for j in range(n2)]
    c = 0
    for i in range(n1):
        for j in range(m1):
            mat1[i][j] = arr1[c]
            c = c+1
    d = 0
    for i in range(n2):
        for j in range(m2):
            mat2[i][j] = arr2[d]
            d += 1
    c = [[0 for i in range(m2)] for j in range(n1)]
    if m1 == n2:
        for i in range(n1):
            for j in range(m2):
                for k in range(n2):
                    c[i][j] += mat1[i][k]*mat2[k][j]
        for i in range(n1):
            for j in range(m2):
                print(c[i][j],end=' ')
        print()
    else:
        print(-1)
    t -= 1
               
            