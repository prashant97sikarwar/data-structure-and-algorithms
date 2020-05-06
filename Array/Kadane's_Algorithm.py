t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    cu = arr[0]
    ma = arr[0]
    for i in range(1,n):
        cu = max(arr[i],cu + arr[i])
        ma = max(ma,cu)
    print(ma)
    t -= 1
    