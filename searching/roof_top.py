t = int(input())
while t > 0:
    n = int(input())
    arr = list(input().split())
    for i in range(n):
        arr[i] = int(arr[i])
    count = 0
    yo = 0
    for i in range(1,n):
        if arr[i] > arr[i-1]:
            count += 1
        else:
            yo = max(yo,count)
            count = 0
    print(max(yo,count))
    t -= 1