#hackerearth problem with the same name

from sys import *
s = stdin.readline()
x,y = 0,0
for i in range(len(s)):
    if s[i] == 'L':
        x -= 1
    elif s[i] == 'R':
        x += 1
    elif s[i] == 'U':
        y += 1
    elif s[i] == 'D':
        y -= 1
print(x,y)