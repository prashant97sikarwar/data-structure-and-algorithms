t = int(input())
while t > 0:
    s = input()
    p = input()
    n = len(p)
    flag = 0
    yup  = 0
    c = p[n-2] + p[n-1] + p
    c = c[0:n]
    if s in c:
        flag = 1
    else:
        d = p + p[0] + p[1]
        d = d[2:]
        if s in d:
            yup = 1
    if (flag or yup):
        print(1)
    else:
        print(0)
    t -= 1