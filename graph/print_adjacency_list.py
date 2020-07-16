
from collections import defaultdict

cases = int(input())
for _ in range(cases):
    v, e = map(int, input().split())

    dic = defaultdict(list)
    
    for _ in range(e):
        a,b = input().split()
        dic[int(a)].append(b)
        dic[int(b)].append(a)

    for k in range(v):
        string = str(k)
        if dic[k]:
            string += '-> ' + '-> '.join(dic[k])
        print(string)