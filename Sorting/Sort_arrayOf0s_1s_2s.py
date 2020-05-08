t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    l = 0
    h = n-1
    m = 0
    while m <= h:
        if arr[m] == 0:
            arr[l],arr[m] = arr[m],arr[l]
            l += 1
            m += 1
        elif arr[m] == 1:
            m += 1
        elif arr[m] == 2:
            arr[m],arr[h] = arr[h],arr[m]
            h -= 1
    for i in range(n):
        print(arr[i],end=' ')
    print()
    t -= 1 