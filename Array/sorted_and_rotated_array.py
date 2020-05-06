t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    l = min(arr)
    flag = 1
    flag1 = 1
    for i in range(n):
        if arr[i] == l:
            min_in =  i
            break
    for i in range(0,min_in-1):
        if arr[i+1] < arr[i]:
            flag = 0
    for i in range(min_in+1,n):
        if arr[i] < arr[i-1]:
            flag1 = 0
    flag2 = 1
    if arr[n-1] > arr[min_in-1]:
        flag2 = 0
    m = max(arr)
    for i in range(n):
        if arr[i] == m:
            max_in = i
            break
    flag3 = 1
    flag4 = 1
    for i in range(0,max_in-1):
        if arr[i+1] > arr[i-1]:
            flag3 = 0
    for i in range(max_in+1,n):
        if arr[i] > arr[i-1]:
            flag4 = 0
    flag5 = 1
    if arr[n-1] < arr[max_in - 1]:
        flag5 =  0
    if (flag and flag1 and flag2) or (flag3 and flag4 and flag5):
        ans = 'Yes'
    else:
        ans = 'No'
    print(ans)
    t -= 1