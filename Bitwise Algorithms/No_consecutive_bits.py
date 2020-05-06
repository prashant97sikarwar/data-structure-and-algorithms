t = int(input())
while t > 0:
    n = int(input())
    if (n & (n >> 1)):
        print(0)
    else:
        print(1)
    t-=1