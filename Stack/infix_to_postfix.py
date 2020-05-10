for t in range(int(input())):
    inp = input()
    stack=[]
    priority = {'^':4,'/':3,'*':3,'+':2,'-':2,'(':1,')':1}
    ans=''
    for elem in inp:
        if(elem not in priority.keys()):
            ans+=str(elem)
        else:
            if(elem==')'):
                while(stack!=None):
                    popped=stack.pop()
                    if(popped=='('):
                        break
                    else: ans+=str(popped)
            elif(elem=='('):
                stack.append(elem)
            else:
                while(stack and stack[-1]!='(' and priority[stack[-1]]>=priority[elem] ):
                    ans+=stack.pop()
                stack.append(elem)
    while(stack):
        ans+=stack.pop()
    print(ans)