t = int(input())
while t > 0:
    n = int(input())
    if n==0:
        ans = "NO"
    elif (n & (n-1)) == 0:
        ans = 'YES'
    else:
        ans = "NO"
    print(ans)
    t -= 1