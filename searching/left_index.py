t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    x = int(input())
    for i in range(n):
        if arr[i] == x:
            ans = i
            break
    print(ans)
    t -= 1