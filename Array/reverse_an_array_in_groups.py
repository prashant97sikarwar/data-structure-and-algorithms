t = int(input())
while t > 0:
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    for i in range(0,n-1,k):
        l= i
        r = min(i+k-1,n-1)
        while l<r:
            arr[l],arr[r] = arr[r],arr[l]
            l += 1
            r -= 1
    for i in range(n):
        print(arr[i],end=' ')
    print()
    t -= 1
    