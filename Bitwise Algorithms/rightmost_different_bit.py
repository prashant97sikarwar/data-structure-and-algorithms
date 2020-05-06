while t > 0:
    n,k = map(int,input().split())
    ref = (n ^ k)
    ans = 1
    if ref == 0:
        ans = 0
    else:
        for i in range(32):
            if (not(ref & 1<<i)):
                ans+=1
            else:
                break
    print(ans)
    t-=1