t = int(input())
while t > 0:
    s = input()
    l = []
    l.append('$')
    n = len(s)
    for i in range(n):
        if l[-1] == s[i]:
            l.pop()
        else:
            l.append(s[i])
    if len(l) == 1:
        print('$')
    else:
        l.pop(0)
        for i in range(len(l)):
            print(l[i],end='')
        print()
    t -= 1