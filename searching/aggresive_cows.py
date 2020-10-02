import math

def isValid(arr,c,n,mid):
    count = 0
    prev = -math.inf
    for i in range(n):
        if arr[i] - prev >= mid:
            count += 1
            prev = arr[i]
    if count >= c:
        return True
    return False
    


def getAns(arr,c,n):
    low = 0
    high = arr[n-1] - arr[0]
    ans = 0
    while low <= high:
        mid = low + (high-low)//2
        if isValid(arr,c,n,mid):
            ans = max(ans,mid)
            low = mid+1
        else:
            high = mid-1
    return ans
t = int(input())
while t > 0:
    n,c = map(int,input().split())
    arr = []
    for i in range(n):
        inp = int(input())
        arr.append(inp)
    arr.sort()
    print(getAns(arr,c,n))
    t -= 1