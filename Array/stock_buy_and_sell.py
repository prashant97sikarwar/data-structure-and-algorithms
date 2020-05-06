def yoyo(arr,n):
    flag = 0
    for i in range(n-1):
        if arr[i+1] <= arr[i]:
            flag = 1
        else:
            flag = 0
            break
    if flag == 1:
        ans = 'No Profit'
        print(ans)
    else:
        i = 0
        li = []
        while i < n-1:
            if arr[i+1] > arr[i]:
                l = i
                j = i+1
                while arr[j] > arr[j-1] and j < n-1:
                    j += 1
                if j == n-1:
                    m = j
                else:
                    m = j-1
                i = j
                li.append((l,m))
            else:
                i += 1
        for i in range(len(li)):
            print(li[i],end=' ')
t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    yoyo(arr,n)
    t -= 1
            