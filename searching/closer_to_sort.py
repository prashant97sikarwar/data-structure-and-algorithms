t = int(input())
while t > 0:
    n = int(input())
    arr = list(input().split())
    for i in range(n):
        arr[i] = int(arr[i])
    x = int(input())
    flag = 0
    for i in range(n):
        if arr[i] == x:
            print(i)
            flag = 1
            break
    if flag == 0:
        print(-1)
    t -= 1