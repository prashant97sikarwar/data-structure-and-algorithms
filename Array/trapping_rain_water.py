def yoyo(arr,n):
    arl = [0]*n
    arf = [0]*n
    sup = arr[0]
    lol = arr[n-1]
    arf[n-1] = lol
    arl[0] = sup
    for i in range(1,n):
        if arr[i] < sup:
            arl[i] = sup
        else:
            sup = arr[i]
            arl[i] = sup
    for i in range(n-2,-1,-1):
        if arr[i] < lol:
            arf[i] = lol
        else:
            lol = arr[i]
            arf[i] = lol
    for i in range(n):
        arr[i] = min(arf[i],arl[i]) - arr[i]
    ans = sum(arr)
    return  ans
t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    yup = yoyo(arr,n)
    print(yup)
    t -= 1
        