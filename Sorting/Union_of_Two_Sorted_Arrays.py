t = int(input())
while t > 0:
    n,m = map(int,input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    s = set()
    arr = arr1 + arr2
    for i in range(n+m):
        if arr[i] not in s:
            s.add(arr[i])
        else:
            arr[i] = -arr[i]
    for i in range(n+m):
        if arr[i] >= 0:
            print(arr[i],end=' ')
    print()
    t -= 1