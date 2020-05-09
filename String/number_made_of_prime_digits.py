import math 
def nthprime(n): 
    len = 1
    prev_count = 0
    while(1):  

        curr_count = (prev_count + 
                      math.pow(4, len))
        if (prev_count < n and 
            curr_count >= n): 
            break
 
        len += 1
  
        prev_count = curr_count 
 
    for i in range (1, len + 1): 
        for j in range(1, 5):  
            if (prev_count + pow(4, len - i) < n):
                prev_count += pow(4, len - i)
 
            else: 
                if (j == 1):
                    print("2", end = "")
                elif (j == 2): 
                    print("3", end = "")
                elif (j == 3): 
                    print("5", end = "")
                elif (j == 4): 
                    print("7", end = "")
                break
    print()
t = int(input())
while t > 0:
    n = int(input())
    nthprime(n)
    t -= 1