def fun(s):
    s = s.lower()
    l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in l:
        if i not in s:
            return 0
    return 1
    
t = int(input())
while t > 0:
    s = input()
    print(fun(s))
    t -= 1
    