def modin(a,b):
    if a == 0:
        return 0,1
    else:
        x1,y1 = modin(b%a,a)
        x = y1 - (b//a) * x1 
        y = x1
    return x,y
        

n = int(input())
num = list(map(int,input().split()))
rem = list(map(int,input().split()))
prod = 1
for i in range(n):
    prod *= num[i]

result = 0
for i in range(n):
    pp = prod//num[i]
    inv,h = modin(pp,num[i])
    if inv < 0:
        inv += num[i]
    print(inv)
    result += (rem[i] * pp *  inv)
print(result%prod)