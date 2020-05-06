def setbits(n):
    count = 0
    while n > 0:
        n = n & (n-1)
        count += 1
    return count
t = int(input())
while t > 0:
    a,b = map(int,input().split())
    s = a ^ b
    ans = setbits(s)
    print(ans)
    t -= 1