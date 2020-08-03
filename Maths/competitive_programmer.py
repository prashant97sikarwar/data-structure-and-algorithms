from sys import *
t = int(stdin.readline())
while t > 0:
    n = input()
    zero = 0
    even = 0
    sm = 0
    for i in n:
        if int(i) == 0:
            zero += 1
        elif int(i)%2 == 0:
            even += 1
        sm += int(i)
    if sm % 3 == 0 and zero > 0 and even > 0:
        print("red")
    elif sm % 3 == 0 and zero > 1 and even == 0:
        print("red")
    else:
        print("cyan")
    t -= 1