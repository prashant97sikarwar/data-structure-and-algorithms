from collections import Counter
t = int(input())
while t > 0:
    s = input()
    p = input()
    a = Counter(s)
    b = Counter(p)
    v = []
    v1 = []
    for i in s:
        v.append(a[i])
    for j in p:
        v1.append(b[j])
    if v == v1:
        print(1)
    else:
        print(0)
    t -= 1