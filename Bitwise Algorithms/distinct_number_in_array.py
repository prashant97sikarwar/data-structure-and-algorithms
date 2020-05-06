    from sys import *
    t = int(stdin.readline())
    while t > 0:
        n = int(stdin.readline())
        arr = list(map(int,stdin.readline().split()))
        xor = 0
        for i in arr:
            xor = xor ^ i
        if xor == 0:
            print(-1)
        else:
            print(xor)
        t -= 1