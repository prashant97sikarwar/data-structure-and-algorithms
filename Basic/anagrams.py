from sys import *
t  = int(stdin.readline())
while t > 0:
    a = stdin.readline()
    b = stdin.readline()
    d1 = dict()
    d2 = dict()
    ans = 0
    if len(a) == 0:
        ans = len(b)
    elif len(b) == 0:
        ans = len(a)
    else:
        for i in range(len(a)):
            if a[i] not in d1:
                d1[a[i]] = 1
                d2[a[i]] = 0
            else:
                d1[a[i]] += 1
        for i in range(len(b)):
            if b[i] not in d2:
                d2[b[i]] = 1
                if b[i] not in d1:
                    d1[b[i]] = 0
            else:
                d2[b[i]] += 1
        for i in d1:
            if d1[i] != d2[i]:
                ans += abs(d1[i] - d2[i])
    print(ans)
    t -= 1