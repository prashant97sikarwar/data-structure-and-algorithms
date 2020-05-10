
def pop1(a):
    global top1
    if top1 >=0:
        x = a[top1]
        top1 -= 1
    else:
        x = -1
    return x
def pop2(a):
    global top2
    if top2 < 101:
        x = a[top2]
        top2 += 1
    else:
        x = -1
    return x
def push1(a,x):
    global top1
    top1 += 1
    a[top1] = x
        
def push2(a,x):
    global top2
    top2 -= 1
    a[top2] = x
