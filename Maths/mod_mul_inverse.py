#function to find modulas multiplicative inverse of "a" under b where "a" and "b" are coprime

def modmulin(a,b):
    if a == 0:
        return b,0,1
    else:
        gcd,x1,y1 = modmulin(b%a,a)
        x = y1 - (b//a) * x1
        y = x1
        return gcd,x,y

m,n = map(int,input().split())
gcd, x,y = modmulin(m,n)
print((x%n+n)%n)
