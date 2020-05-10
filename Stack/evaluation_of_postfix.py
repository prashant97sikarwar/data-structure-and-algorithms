t = int(input())
while t > 0:
    s = input()
    l = []
    for i in s:
        if i.isdigit():
            l.append(i)
        else:
            val1 = l.pop()
            val2 = l.pop()
            l.append(str(int(eval(val2 + i + val1))))
    print(l[-1])
    t -=  1