import math

def muy_fun(num):
    result = num
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            while num % i == 0:
                num = num//i
            result = result * (1.0 - (1.0/i))
    if num > 1:
        result = result * (1.0 -(1.0/num))
    return int(result)
        
t = int(input())
while t > 0:
    n = int(input())
    print(muy_fun(n))
    t -=1 