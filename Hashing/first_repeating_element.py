t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    s = dict()
    for i in range(n):
        if arr[i] in s.keys():
            s[arr[i]] += 1
        else:
            s[arr[i]] = 1
    for i in range(n):
        if s[arr[i]] > 1:
            ans = i+1
            break
        else:
            ans = -1
    print(ans)
    t -= 1 