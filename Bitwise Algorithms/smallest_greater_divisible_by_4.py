from sys import *


def fun(n):
    p = [0 for i in range(n+2)]
    index = 0
    x = n
    while x > 0:
        p[index] = x % 4
        x = x//4
        index += 1
    idx = 0
    for i in range(len(p)-1):
        if p[i] > 1:
            p[i] = 0
            p[i+1] += 1
            for j in range(idx, i):
                p[j] = 0
            idx += 1
        '''if p[i] >= 4:
            p[i] = 0
            p[i+1] += 1'''
    j = len(p) - 1
       if (p[j] >= 2):
            p[index] = 1
            index += 1
        ans = 0
    i = len(p)-1
        while(i >= 0):
            ans = ans * 4 + p[i]
            i -= 1
        print(ans)


t = int(stdin.readline())
while t > 0:
    n = int(stdin.readline())
    fun(n)
    t -= 1
