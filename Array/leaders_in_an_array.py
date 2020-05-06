t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    l = []
    yol = arr[n-1]
    l.append(yol)
    for i in range(n-2,-1,-1):
        if arr[i] >= yol:
            l.append(arr[i])
        yol = max(yol,arr[i])
    l = l[::-1]
    for i in range(len(l)):
        print(l[i],end=' ')
    print()
    t -= 1