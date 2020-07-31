def modexpo(x,n,m):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return modexpo(x*x % m,n//2,m)
    elif n % 2 == 1:
        return (x%m * modexpo(x*x % m, n//2,m)) % m

x,n,m = map(int,input().split())
print(modexpo(x,n,m))