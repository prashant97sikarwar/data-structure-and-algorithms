'''print the maximum value of |arr[i]-arr[j]| + |i-j| in a given array arr. '''
from sys import *
t = int(stdin.readline())
while t > 0:
    n = int(stdin.readline())
    a = list(map(int,stdin.readline().split()))
    first = []
    second = []
    for i in range(n):
        first.append(a[i] + i)
    for i in range(n):
        second.append(a[i] - i)
    mx1 = max(first)
    mn1 = min(first)
    ans1 =  mx1 - mn1
    mx2 = max(second)
    mn2 = min(second)
    ans2 = mx2 - mn2
    print(max(ans1,ans2))
    t -= 1