from sys import *
def check(arr,n):
    ans = 0
    for i in range(32):
        count = 0
        for j in range(n):
            if (arr[j] & (1<<i)):
                count += 1
        subset = (1 << count) - 1
        subset = subset * (1 << i)
        ans += subset
    return ans%1000000007

t = int(stdin.readline())
while t > 0:
    n = int(stdin.readline())
    arr = list(map(int,stdin.readline().split()))
    print(check(arr,n))
    t -= 1 

