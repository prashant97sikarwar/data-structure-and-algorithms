t = int(input())
while t > 0:
    s = input()
    n = len(s)
    l = []
    l.append('$')
    for i in range(n):
        if l[-1] == s[i]:
            continue
        else:
            l.append(s[i])
    l.pop(0)
    for i in range(len(l)):
        print(l[i],end='')
    print()
    t -= 1
        