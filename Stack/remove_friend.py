from sys import *
t = int(stdin.readline())
while t > 0:
    n,k = map(int,stdin.readline().split())
    arr = list(map(int,stdin.readline().split()))
    l = []
    for i in range(n):
        while(len(l) != 0 and k > 0 and l[-1] < arr[i]):
            l.pop(-1)
            k -= 1
        l.append(arr[i])
    while k > 0:
        l.pop(-1)
        k -= 1
    for i in range(len(l)):
        print(l[i],end=' ')
    print()
    t -= 1