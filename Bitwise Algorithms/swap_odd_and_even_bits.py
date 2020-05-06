t = int(input())
while t > 0:
    n = int(input())
    even = n & 0xAAAAAAAA
    odd = n & 0x55555555
    even >>= 1
    odd <<= 1
    ans = even | odd
    print(ans)
    t -= 1