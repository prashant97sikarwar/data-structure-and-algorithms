t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    arr=sorted(arr, key=arr.count,reverse=True)
    for i in range(n):
        print(arr[i],end=' ')
    print()
    t -= 1