while t > 0:
    n = int(input())
    k = int(input())
    p = 1<<k
    if (n & p):
        print('Yes')
    else:
        print('No')
    t-=1