def gcd(m,n):
    if m == 0:
        return n
    if n == 0:
        return m
    return gcd(n,m%n)

m,n = map(int,input().split())
print(gcd(m,n))