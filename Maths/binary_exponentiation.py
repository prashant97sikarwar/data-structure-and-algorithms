def expo(m,n):
    if n == 2:
        return m * m
    elif n % 2 == 0:
        return expo(m*m,n//2)
    elif n % 2 == 1:
        return m * expo(m,n-1)
    
m,n = map(int,input().split())
print(expo(m,n)) 