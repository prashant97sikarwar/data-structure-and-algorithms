def check(arr,n,z):
    do = arr[0]
    for i in range(1,n):
        do = do & z & arr[i]
        if do == 0:
            return "Yes"       
    return "No"
     
from sys import *
t = int(stdin.readline())
while t > 0:
    z,n = map(int,stdin.readline().split())
    arr = list(map(int,stdin.readline().split()))
    print(check(arr,n,z))
    t -= 1