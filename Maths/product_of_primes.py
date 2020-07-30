def find():
    maxx=100001
    isprime=[True]*100001
    prime=[]
    
    p=2
    while (p*p<maxx):
        if isprime[p]==True:
            for i in range(p*p,maxx,p):
                isprime[i]=False
        p+=1
    for i in range(2,maxx):
        if isprime[i]:
            prime.append(i)
    return prime

prime=find()
def fromlr(l,r,prime):
    mark=[True]*(r-l+1)
    prod=1
    for i in range(len(prime)):
        if prime[i]*prime[i]<=r:
            low=(l//prime[i])*prime[i]
            if low<l:
                low+=prime[i]
            for j in range(low,r+1,prime[i]):
                mark[j-l]=False
            if low==prime[i]:
                mark[low-l]=True
  
    for j in range(0,r-l+1):
        if mark[j]==True:
            prod*=(j+l)
    return prod%(10**9+7)
            
            
                
for _ in range(int(input())):
    l,r=map(int,input().split())
    print(fromlr(l,r,prime))