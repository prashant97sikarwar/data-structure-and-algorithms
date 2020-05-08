t = int(input())
while t > 0:
    n,s = map(int,input().split())
    arr = list(map(int,input().split()))
    start = 0
    flag = 0
    cu = 0
    for i in range(n):
        cu += arr[i]
        while cu > s:
            cu -= arr[start]
            start += 1
        if cu == s:
            flag = 1
            print(start+1,end=' ')
            print(i+1)
            break
    if flag == 0:
        print(-1)
    t -= 1