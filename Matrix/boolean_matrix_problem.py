def modifyMatrix(mat,r,c) : 
    row_flag = False
    col_flag = False
    for i in range(0,r) : 
        for j in range(0, c) : 
            if (i == 0 and mat[i][j] == 1) : 
                row_flag = True
            if (j == 0 and mat[i][j] == 1) : 
                col_flag = True
            if (mat[i][j] == 1) : 
                mat[0][j] = 1
                mat[i][0] = 1
    for i in range(1,r) : 
        for j in range(1,c) : 
            if (mat[0][j] == 1 or mat[i][0] == 1) : 
                mat[i][j] = 1
    if (row_flag == True) : 
        for i in range(0,c) : 
            mat[0][i] = 1
    if (col_flag == True) : 
        for i in range(0,r) : 
            mat[i][0] = 1
t = int(input())
while t > 0:
    r,c = map(int,input().split())
    mat = []
    for i in range(r):
        mat.append(list(map(int,input().split())))
    modifyMatrix(mat,r,c)
    for i in range(r):
        for j in range(c):
            print(mat[i][j],end=' ')
        print()
    t-=1