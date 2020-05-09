t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    s = set()  
    d = set()
    pair = False
    for i in range(0, n):  
        if arr[i] > 0:  
            s.add(arr[i]) 
    
    for i in range(0, n):  
        if arr[i] < 0: 
            if (-arr[i]) in s:  
                d.add(-arr[i])
                pair = True
    l = list(d)
    if len(l) > 0:
        l.sort()
        for i in range(len(l)):
            print(l[i],end=' ')
            print(-l[i],end=' ')
        print()
    if pair == False: 
        print(0)
    t -= 1