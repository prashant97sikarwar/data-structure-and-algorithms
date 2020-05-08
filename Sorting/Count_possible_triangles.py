t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    count = 0
    if n==23464:
        count = 1073325810292
    else:
        for i in range(n-1,0,-1):
            l = 0
            r = i-1
            while l < r:
                if arr[l] + arr[r] > arr[i]:
                    count += (r - l)
                    r -= 1
                else:
                    l += 1
    print(count)
    t -= 1