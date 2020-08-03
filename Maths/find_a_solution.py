def exeuclid(a,b):
    if a == 0:
        return b,0,1
    else:
        gcd,x1,y1 = exeuclid(b%a,a)
        x = y1 - (b//a) * x1
        y = x1
    return gcd,x,y

def fun(a,b,c):
    g,x,y = exeuclid(abs(a),abs(b))
    if c % g != 0:
        return False
    x0 = x*c/g
    y0 = y*c/g
    if a < 0:
        x0 = -x0
    if b < 0:
        y0 = -y0
    return x0,y0
        
a,b,c = map(int,input().split())
print(fun(a,b,c))