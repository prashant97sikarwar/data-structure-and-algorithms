t = int(input())
while t > 0:
    n = int(input())
    count = 0
    largest = 0
    while n > 0:
        if (n & 1) == 1:
            count += 1
        else:
            largest = max(largest,count)
            count = 0
        n = n>>1
    largest = max(largest,count)
    print(largest)
    t -= 1