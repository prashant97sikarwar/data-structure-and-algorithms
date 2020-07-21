def largest_palindrome(n):
    sep = 1
    for i in range(n):
        sep = sep * 10 
        upperlimit = sep - 1
        
    lowerlimit = 1 + upperlimit//10
    
    ans = 0
    for i in range(upperlimit,lowerlimit-1,-1):
        for j in range(i,lowerlimit-1,-1):
            product = i * j
            if product < ans:
                break
            number = product
            reverse = 0
            while (number != 0):
                reverse = 10 * reverse + number % 10
                number = number//10
            if product == reverse and product > ans:
                ans = product
    return ans
    
t = int(input())
while t > 0:
    n = int(input())
    print(largest_palindrome(n))
    t -= 1 