t = int(input())
while t >0:
    n = int(input())
    arr = list(map(int,input().split()))
    maj = 0
    count = 1
    for i in range(1,n):
        if arr[i] == arr[maj]:
            count += 1
        else:
            count -= 1
        if count == 0:
            maj = i
            count = 1
    loop = 0
    for i in range(n):
        if arr[i] == arr[maj]:
            loop += 1
    if loop > n//2:
        ans = arr[maj]
    else:
        ans = -1
    print(ans)
    t -= 1