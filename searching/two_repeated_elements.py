t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    s = set()
    for i in range(n+2):
        if arr[i] not in s:
            s.add(arr[i])
        else:
            print(arr[i],end=' ')
    print()
    t-=1