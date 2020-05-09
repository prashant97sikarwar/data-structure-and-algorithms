t = int(input())
while t > 0:
    n,m = map(int,input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    arr = arr1 + arr2
    s = set()
    for i in range(n+m):
        if arr[i] not in s:
            s.add(arr[i])
        else:
            arr[i] = -arr[i]
    l = list(s)
    print(len(l))
    t -= 1
        