def binary(arr,l,r,k):
    if l <= r:
        mid = l + (r-l)//2
        if arr[mid] == k:
            return 1
        elif arr[mid] > k:
            return binary(arr,l,mid-1,k)
        else:
            return binary(arr,mid+1,r,k)
    else:
        return -1
t = int(input())
while t > 0:
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    l = 0
    r = n-1
    print(binary(arr,l,r,k))
    t-=1
    