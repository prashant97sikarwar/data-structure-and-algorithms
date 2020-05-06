t = int(input())
while t > 0:
    n = int(input())
    if n == 0:
        ans = 0
    else:
        for i in range(61):
            if (n & (1<<i)):
                ans = i + 1
                break
    print(ans)
    t -= 1
            