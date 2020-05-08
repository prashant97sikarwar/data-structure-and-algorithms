t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    count = 1
    s = set()
    for i in range(n):
        if arr[i] not in s:
            s.add(arr[i])
        else:
            count += 1
            p = arr[i]
    print(p,end=' ')
    print(count)
    t-=1