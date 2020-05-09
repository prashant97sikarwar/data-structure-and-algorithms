t = int(input())
while t > 0:
    n,m = map(int,input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    arr1.sort()
    arr2.sort()
    count = 0
    i = 0
    j = 0
    s = set()
    while i < n and j < m:
        if arr1[i] == arr2[j]:
            s.add(arr1[i])
            i += 1
            j += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            i += 1
    l = list(s)
    print(len(l))
    t -= 1