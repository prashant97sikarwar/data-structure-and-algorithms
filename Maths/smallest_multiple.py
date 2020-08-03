def gcd(a,b):
    if a == 0:
        return b
    else:
        return gcd(b%a,a)

def lcm(a,b):
    return (a/gcd(a,b))*b
    
curr = lcm(1,2)
for i in range(3,28):
    curr = lcm(curr,i)
    
print(int(curr))