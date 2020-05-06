from sys import *
t = int(stdin.readline())
while t > 0:
    a,b = map(int,stdin.readline().split())
    if a == b:
        print(a)
    elif b-a == 1:
        print(b & (b-1))
    else:
        ans = (b & b-1)
        ans = max(ans,(b-1) & (b-2))
        print(ans)
    t-=1