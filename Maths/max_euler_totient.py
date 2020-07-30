def sieve(num):
    l = []
    mark = [True for i in range(num+1)]
    p = 2
    while p * p <= num:
        if mark[p] == True:
            for i in range(p*p,num+1,p):
                mark[i] = False
        p += 1
    for i in range(2,num+1):
        if mark[i]:
            l.append(i)
    return l
    
t = int(input())
while t > 0:
    n = int(input())
    l = sieve(40)
    res = 1
    for i in range(len(l)):
        if res * l[i] <= n:
            res = res * l[i]
    print(res)
    t -=1 
        