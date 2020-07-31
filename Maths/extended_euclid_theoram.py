def exeuclid(a,b):
    if a == 0:
        return b,0,1
    else:
        gcd,x1,y1 = exeuclid(b%a,a)
        x = y1 - (b//a) * x1
        y = x1
    return gcd,x,y

m,n = map(int,input().split())
print(exeuclid(m,n))
        
        