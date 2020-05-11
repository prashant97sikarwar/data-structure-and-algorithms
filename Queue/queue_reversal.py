def reverseQueue(q):
    return q[::-1]

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        q=list(map(int,input().split()))
        q=reverseQueue(q)
        for i in q:
            print(i,end=" ")
        print()