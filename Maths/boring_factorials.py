from sys import *
t = int(stdin.readline())
while t > 0:
    n,p = map(int,stdin.readline().split())
    if n >= p:
        print(0)
    else:
        ans = 1
        for i in range(n+1,p):
            depx = pow(i,p-2,p)
            ans = (ans*depx)%p
        print(p - ans)
    t -= 1