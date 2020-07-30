from sys import *
import math
prime = []

def sieve(num):
    p = 2
    mark = [True for i in range(num + 1)]
    while p * p <= num:
        if mark[p] == True:
            for j in range(p*p,num+1,p):
                mark[j] = False
        p += 1
    for i in range(2,num+1):
        if mark[i] == True:
            print(i,end=' ')
            prime.append(i)


def segmentedsieve(n):
    limit = int(math.floor(math.sqrt(n)) + 1)
    sieve(limit)
    low = limit
    high = limit * 2
    while low < n:
        if high >= n:
            high = n
        mark = [True for i in range(limit + 1)]
        for i in range(len(prime)):
            var = int((low//prime[i]) * prime[i])
            if var < low:
                var = var + prime[i]
            for j  in range(var,high,prime[i]):
                mark[j-low] = False
        for i in range(low,high):
            if mark[i-low]:
                print(i,end=' ')
        low = low + limit
        high = high + limit
        
n = int(stdin.readline())
segmentedsieve(n)