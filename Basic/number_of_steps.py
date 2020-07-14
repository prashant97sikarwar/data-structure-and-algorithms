from sys import *
n = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))
brr = list(map(int,stdin.readline().split()))
count = 0
mn = min(arr)
for k,v  in enumerate(arr):
    while v > mn and v >= brr[k] and brr[k] > 0:
        v -= brr[k]
        arr[k] = v
        count += 1
    if v < mn and mn > 0:
        mn = v
        for i in range(k):
            while arr[i] > mn and arr[i] > brr[i] and brr[i] > 0:
                arr[i] -= brr[i]
                count += 1
if len(set(arr)) == 1:
    print(count)
else:
    print(-1)
