t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    s = set()
    ans = 0
    for i in range(n):
        s.add(arr[i])
    for i in  range(n):
        if (arr[i] - 1) not in s:
            j = arr[i]
            while (j in s):
                j += 1
            ans = max(ans,j-arr[i])
    print(ans)
    t -= 1