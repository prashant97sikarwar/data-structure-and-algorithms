t = int(input())
while t > 0:
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    arr = sorted(arr)
    for i in range(k):
        print(arr[-1],end=' ')
        arr.pop()
    print()
    t -= 1