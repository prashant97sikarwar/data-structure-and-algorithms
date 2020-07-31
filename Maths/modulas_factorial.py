def fact(n):
    res = 1
    for i in range(2,n+1):
        res = (res*i)%1000000007
    return res
    
m = fact(25)
l = fact(75)
po = 1000000007
print(((m%po)*(l%po))%po)
