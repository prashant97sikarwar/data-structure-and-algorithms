for _ in range(int(input())):
    n=int(input())
    k=int(input())
    a=[[] for i in range(n)]
    for i in range(k):
        x,y=map(int,input().split())
        a[x].append(y)
        a[y].append(x)
    vis=[0]*n
    st=[]
    size=[]
    for i in range(n):
        if vis[i]==0:
            vis[i]=1
            st.append(i)
        s=0
        while st:
            p=st.pop(0)
            s+=1
            for j in a[p]:
                if vis[j]==0:
                    vis[j]=1
                    st.append(j)
        if s:
            size.append(s)
    print(len(size))
    size.sort()
    print(*size)
        