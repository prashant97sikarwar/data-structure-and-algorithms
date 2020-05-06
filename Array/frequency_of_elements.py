t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    for i in range(n):
        arr[i] = arr[i] - 1
    for i in range(n):
        arr[arr[i] % n] += n
    for i in range(n):
        print(arr[i]//n,end = ' ')
    print()
    t -= 1