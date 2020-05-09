t = int(input())
while t > 0:
    s = input()
    d = dict()
    for i in range(len(s)):
        if s[i] in d.keys():
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    ma = max(d.values())
    l = []
    for i in range(len(s)):
        if d[s[i]] == ma:
            l.append(int(s[i]))
    
    print(max(l))
    t -= 1
    