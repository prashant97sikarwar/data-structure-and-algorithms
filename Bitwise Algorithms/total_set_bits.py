def fun(n):
    count = 0
    while n > 0:
        n = n & (n-1)
        count += 1
    return count
t = int(input())
while t > 0:
    n = int(input())
    dep = 0
    for i in range(1,n+1):
        dep += fun(i)
    print(dep)
    t -= 1 