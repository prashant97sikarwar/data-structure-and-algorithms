t = int(input())
while t > 0:
    n,m = map(int,input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    arr = [0] * (n+m)
    i = 0
    j = 0
    k = 0
    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1
    while i < n:
        arr[k] = arr1[i]
        i += 1
        k += 1
    while j < m:
        arr[k] = arr2[j]
        j += 1
        k += 1
    l = n+m
    if (l) % 2==1:
        print(arr[int((l+1)/2) - 1])
    else:
        ans = ((arr[(l//2)-1]) + (arr[(l//2)+1-1]))//2
        print(ans)
    t -= 1