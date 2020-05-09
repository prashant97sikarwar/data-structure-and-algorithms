t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(str,input().strip().split()))
    d = dict()
    for i in range(n):
        if arr[i] in d.keys():
            d[arr[i]] += 1
        else:
            d[arr[i]] = 1
    ans = max(d.values())
    for x in sorted(list(d.keys())):
        if d[x] == ans:
            print(x,end=' ')
            print(ans)
            break
    t -=1 
        