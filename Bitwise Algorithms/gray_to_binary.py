t = int(input())
while t > 0:
    n = int(input())
    inv = 0
    while(n): 
        inv = inv ^ n
        n = n >> 1
    print(inv) 
    t -= 1