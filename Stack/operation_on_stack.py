def insert(stack,x):
    stack.append(x)

def find(stack,x):
    for i in range(len(stack)):
        if stack[i] == x:
            return 1
    return 0
    
def headOf_Stack(stack):
    if len(stack) == 0:
        return -1
    else:
        return stack[len(stack) - 1]
    
def remove(stack):
    if len(stack) == 0:
        return -1
    else:
        return stack.pop()