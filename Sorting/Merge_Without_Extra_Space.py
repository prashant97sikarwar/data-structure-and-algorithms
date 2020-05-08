t = int(input())
while t > 0:
    x,y = map(int,input().split())
    arr = list(map(int,input().split()))
    arr1 = list(map(int,input().split()))
    i = 0
    j = 0
    while i < x and j < y:
        if arr[i] < arr1[j]:
            print(arr[i],end=' ')
            i += 1
        else:
            print(arr1[j],end=' ')
            j += 1
    while i < x:
        print(arr[i],end=' ')
        i += 1
    while j < y:
        print(arr1[j],end=' ')
        j += 1
    print()
    t -= 1