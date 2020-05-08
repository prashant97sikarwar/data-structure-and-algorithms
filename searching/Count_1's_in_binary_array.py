def count(arr,l,h): 
    if h>=l: 
        mid = l + (h-l)//2
        if ((mid == h or arr[mid+1]==0) and (arr[mid]==1)): 
            return mid+1
        if arr[mid]==1: 
            return count(arr, (mid+1), h) 
        return count(arr, l, mid-1) 
    return 0

t = int(input())
while t > 0:
    n = int(input())
    arr = list(input().split())
    for i in range(n):
        arr[i] = int(arr[i])
    l = 0
    r = n-1
    print(count(arr,l,r))
    t -= 1    