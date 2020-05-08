t = int(input())
while t > 0:
    n = int(input())
    arr =  list(map(int,input().split()))
    k = int(input())
    arr.sort()
    print(arr[k-1])
    t-=1