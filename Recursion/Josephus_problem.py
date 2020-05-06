def jos(n,k):
    if n==1:
        return n
    else:
        return (jos(n-1,k) + k-1) % n + 1
t = int(input())
while t > 0:
    n,k = map(int,input().split())
    print(jos(n,k))
    t -= 1
