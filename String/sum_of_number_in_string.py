import re
t = int(input())
while t > 0:
    s = input()
    temp = re.findall('\d+',s)
    ans = list(map(int,temp))
    print(sum(ans))
    t -= 1