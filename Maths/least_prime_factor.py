def ans(n):
    arr = [0 for i in range(n+1)]
    arr[1] = 1
    for i in range(2,n+1):
        if arr[i] == 0:
            arr[i] = i
            for j in range(2*i,n+1,i):
                if arr[j] == 0:
                    arr[j] = i
    return arr
t = int(input())
while t > 0:
    n = int(input())
    arr = ans(n)
    for i in range(1,n+1):
        print(arr[i],end=' ')
    print()
    t -= 1
    