import math

def largest_prime_factor(n):
    while n % 2 == 0:
        p = 2
        n = n >> 1
    for i in range(3,int(math.sqrt(n)),2):
        while n % i == 0:
            p = i
            n = n//i
    if n > 2:
        p = n
    return p
        

n = 13195
print(largest_prime_factor(n))