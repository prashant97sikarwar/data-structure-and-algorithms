def check(s):
    l = []
    n = len(s)
    for i in range(n):
        if s[i] =='{' or s[i]=='[' or s[i] == '(':
            l.append(s[i])
            continue
        if len(l) == 0:
            return False
        if s[i] == ')':
            x = l.pop()
            if x == '{' or x == '[':
                return False
        elif s[i] == '}':  
            x = l.pop()
            if (x == '(' or x == '[') : 
                return False;  
        elif s[i] == ']':  
            x = l.pop()
            if (x =='(' or x == '{') : 
                return False;  
    if len(l) == 0:
        return True
    else:
        return False
t = int(input())
while t > 0:
    s = input()
    if (check(s)):
        print('balanced')
    else:
        print('not balanced')
    t -= 1
    
        
    