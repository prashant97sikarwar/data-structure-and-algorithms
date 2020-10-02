import math
def check(arr,n,m,mid):
    sm = 0
    for i in range(n):
        if arr[i] > mid:
            sm += arr[i] - mid
    return sm

n,m = map(int,input().split())
arr = list(map(int,input().split()))
def ans(arr,n,m):
    low = 0
    high = max(arr)
    ans = -math.inf
    while low <= high:
        mid = low + (high - low)//2
        if check(arr,n,m,mid) >= m:
            ans = max(ans,mid)
            low = mid+1
        else:
            high = mid-1
    return ans
print(ans(arr,n,m))