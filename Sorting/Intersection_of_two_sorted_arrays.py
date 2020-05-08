t = int(input())
while t > 0:
    n,m = map(int,input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    i = 0
    j = 0
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] == arr2[j]:
            print(arr1[i],end=' ')
            i += 1
            j += 1
        else:
            j += 1
    print()
    t -= 1