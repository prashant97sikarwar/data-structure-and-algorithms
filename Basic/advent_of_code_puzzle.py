from sys import *
s = stdin.readline()
ans = 0
for i in range(len(s)):
    if s[i] == '(':
        ans += 1
    if s[i] == ')':
        ans -= 1
    if ans == -1:
        ty = i + 1
        break
print(ty)