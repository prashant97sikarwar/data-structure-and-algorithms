t = int(input())
while t > 0:
    n = input()
    arr = list(map(int,input().split()))
    x = int(input())
    for i in range(len(arr)):
        if arr[i] == x:
            ans = i
            break
        else:
            ans = -1
    print(ans)
    t -= 1