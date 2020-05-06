def rearrange(arr,n):
    mii = 0
    mai = n-1
    ma = arr[n-1] + 1
    for i in range(n):
        if i % 2 == 0:
            arr[i] += (arr[mai]%ma) * ma
            mai -= 1
        else:
            arr[i] += (arr[mii] % ma) * ma
            mii += 1
    for i in range(n):
        arr[i] = arr[i]//ma
    return arr
t = int(input())
while t > 0:
    n = int(input())
    arr = list(input().split())
    for i in range(n):
        arr[i] = int(arr[i])
    rearrange(arr,n)
    for i in range(n):
        print(arr[i],end =' ')
    print()
    t -= 1