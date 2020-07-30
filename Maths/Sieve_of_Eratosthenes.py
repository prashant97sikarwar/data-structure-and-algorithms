def fun(n):
    p  = 2
    arr = [False for i in range(n+1)]
    while p * p <= n:
        if arr[p] == False:
            for i in range(p*p,n+1,p):
                arr[i] = True
        p += 1
    
    for i in range(2,len(arr)):
        if arr[i] == False:
            print(i,end=' ')
    
t = int(input())
while t > 0:
    n  = int(input())
    fun(n)
    print()
    t -= 1