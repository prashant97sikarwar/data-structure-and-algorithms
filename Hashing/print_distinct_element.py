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
    for i in range(n):
        if dic[arr[i]] == 1:
            print(arr[i],end=' ')
    print()
    t -= 1 
    