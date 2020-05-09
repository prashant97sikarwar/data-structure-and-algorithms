t = int(input())
while t > 0:
    s = input()
    p = input()
    ans = 100000
    flag = 0
    for i in p:
        ind = s.find(i)
        if  ind != -1:
            ans = min(ind,ans)
            flag = 1
    if flag == 1:
        print(s[ans])
    else:
        print('$')
    t -= 1