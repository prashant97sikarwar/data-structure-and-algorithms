t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    flag = 0
    if n == 1:
        flag = 2
    for i in range(1,n):
        arr[i] = arr[i] + arr[i-1]
    for i in range(1,n):
        if (arr[n-1] - arr[i]) == arr[i-1]:
            flag = 1
            break
    if flag == 0:
        ans = -1
    elif flag == 2:
        ans = 1
    else:
        ans = i + 1
    print(ans)
    t -= 1