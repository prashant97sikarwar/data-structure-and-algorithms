from sys import *
def check(l):
    l = bin(l)[2:]
    count = 0
    for i in l:
        if i is '0':
            count += 1
    count += (6-len(l))
    return count
t = int(stdin.readline())
while t > 0:
    s = input()
    des = 1
    for i in range(len(s)):
        if s[i].isdigit() == False and s[i].isupper():
            l = ord(s[i]) - 55
        elif s[i].isdigit():
            l = int(s[i])
        elif s[i] == '-':
            l = 62
        elif s[i] == '_':
            l = 63
        else:
            l = ord(s[i]) - 61
        flag = check(l)
        ans = 3**flag
        des = des * ans
    print(des%1000000007)
    t-=1
