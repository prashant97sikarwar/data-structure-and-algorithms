t = int(input())
while t > 0:
    n = int(input())
    s = input()
    l = []
    r = []
    flag = [False]*n
    for i in range(n):
        if s[i].isupper():
            l.append(s[i])
            flag[i] = True
        else:
            r.append(s[i])
    r.sort()
    l.sort()
    s1 = 0
    arr = []
    s2 = 0
    for i in range(n):
        if flag[i] is True:
            arr.append(l[s1])
            s1 += 1
        else:
            arr.append(r[s2])
            s2 += 1
    st = ''
    print(st.join(arr))
    t -= 1
            