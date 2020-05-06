t = int(input())
while t > 0:
    n = int(input())
    arr = list(input().split())
    for i in range(0,n-1,2):
        arr[i],arr[i+1] = arr[i+1],arr[i]
    for i in range(n):
        print(arr[i],end=' ')
    print()
    t -= 1 