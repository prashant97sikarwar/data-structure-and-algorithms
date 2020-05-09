t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    dic = {}
    for i in range(n):
        if arr[i] in dic.keys():
            dic[arr[i]] += 1
        else:
            dic[arr[i]] = 1
    count = 0
    for x in dic:
        if dic[x] == 1:
            count += 1
    print(count)
    t -= 1 
    