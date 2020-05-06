t = int(input())
while t > 0:
    n,d = map(int,input().split())
    arr = list(map(int,input().split()))
    temp = []
    for i in range(d):
        temp.append(arr[i])
    for i in range(n-d):
        arr[i] = arr[i+d]
    del arr[n-d:]
    arr = arr + temp
    for i in range(n):
        print(arr[i],end=' ')
    print()
    t -= 1