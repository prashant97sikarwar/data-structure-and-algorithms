from sys import *
n = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))
k = 2
start = 1 
while start <= n:
    start += k
    k += 1
start -= k-1
k -= 2
s = sum(arr[:start])
mxum = s
for i in range(1,n):
    s -= arr[i-1]
    if start < n:
        s += arr[start]
        start += 1
    else:
        k -= 1
        s -= sum(arr[n-k : n])
        start -= k
    if s > mxum:
        mxum = s
print(mxum)