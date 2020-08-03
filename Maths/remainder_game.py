import math
def lcm(a,b):
    return a*b/int(math.gcd(a,b))

from sys import *
n,k = map(int,stdin.readline().split())
arr = list(map(int,stdin.readline().split()))
curr = 1
for i in range(n):
    curr = int(math.gcd(k,lcm(curr,arr[i])))
if curr == k:
    print("Yes")
else:
    print("No")