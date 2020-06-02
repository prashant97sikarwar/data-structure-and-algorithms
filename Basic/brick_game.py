## hackerearth problem with the same name 

from sys import *
n = int(stdin.readline())
i = 0
while n > 0:
    i += 1
    n = n - i
    if n < 0 or n == 0:
        ans = 'Patlu'
        break
    n = n - 2*i
    if n < 0 or n == 0:
        ans = "Motu"
        break
print(ans)