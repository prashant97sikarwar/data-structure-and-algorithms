t = int(input())
while t > 0:
    s = input()
    p = input()
    for i in range(len(s)):
        if s[i:i+len(p)] == p:
            ans = 'Yes'
            break
        else:
            ans = 'No'
    print(ans)
    t -= 1
