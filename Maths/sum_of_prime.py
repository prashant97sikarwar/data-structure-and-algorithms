def sieve(n,s):
    prime = []
    
    mark = [True for i in range(n+1)]
    p =  2
    while p*p <= n:
        if mark[p] == True:
            for i in range(p*p,n+1,p):
                mark[i] = False
        p += 1
    for i in range(2,len(mark)):
        if mark[i]:
            prime.append(i)
            s.add(i)
    return prime,s
    
def fun(prime,s,n):
    if n <=2 :
        print(-1)
    else:
        flag = 0
        for i in range(len(prime)):
            diff = n - prime[i]
            if diff in s:
                print(prime[i],diff)
                flag = 1
                break
        if flag == 0:
            print(-1)

    

t = int(input())
while t > 0:
    n = int(input())
    s = set()
    prime,s = sieve(n, s)
    fun(prime,s,n)
    t -= 1
            