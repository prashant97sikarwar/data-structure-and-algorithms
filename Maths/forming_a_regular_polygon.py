from sys import *
n = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))
d = dict()
for i in range(n):
    if arr[i] not in d:
        d[arr[i]] = 1
    else:
        d[arr[i]] += 1
ans = 0
for i in d:
    if d[i] == 3:
        ans += 1
    elif d[i] > 3:
        ans += ((2**d[i]) - (d[i]**2 + d[i] + 2)//2)
print(ans%1000000007)