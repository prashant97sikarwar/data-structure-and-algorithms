t = int(input())
while t > 0:
    n,x = map(int,input().split())
    arr = list(map(int,input().split()))
    flag = 0
    for i in range(n-1):
        s = set()
        cu = x - arr[i]
        for j in range(i+1,n):
            if (cu - arr[j]) not in s:
                s.add(arr[j])
            else:
                flag = 1
                break
    if flag == 0:
        print(0)
    else:
        print(1)
    
    t -= 1 