t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    i = 0
    j = n-1
    while i < j:
        if arr[i] > arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
            j -= 1
        elif arr[i] == arr[j] and arr[i] == 0:
            i += 1
        elif arr[i] == arr[j] and arr[i] == 1:
            j -= 1
        else:
            i += 1
            j -= 1
    for i in range(n):
        print(arr[i],end=' ')
    print()
    t -= 1