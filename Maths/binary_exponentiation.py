def expo(m,n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return expo(m*m,n//2)
    elif n % 2 == 1:
        return m * expo(m * m,n-1//2)
    
m,n = map(int,input().split())
print(expo(m,n)) 