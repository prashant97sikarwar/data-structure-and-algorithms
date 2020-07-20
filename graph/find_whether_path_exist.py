false =[]
def traverse(arr,x,y,n):
    stack=[[x,y]]
    v = []
    res = 0
    while(len(stack)>0):
        x,y = stack.pop()
        v.append([x,y])
        if arr[x][y]==2:
            res=1
            break
        if arr[x][y]==0:
            continue
        if x+1<n and [x+1,y] not in v:
            stack.append([x+1,y])
        if x-1>=0 and [x-1,y] not in v:
            stack.append([x-1,y])
        if y+1<n and [x,y+1] not in v:
            stack.append([x,y+1])
        if y-1>=0 and [x,y-1] not in v:
            stack.append([x,y-1])
    return res
T = int(input())
for _ in range(T):
    n = int(input())
    temp = [int(x) for x in input().split()]
    arr=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            arr[i][j]=temp.pop(0)
            if arr[i][j]==1:
                s = [i,j]
    res = traverse(arr,s[0],s[1],n)
    print(int(res))
    false.clear()