from collections import deque
t = int(input())
while t > 0:
    n,k = map(int,input().split())
    arr = list(input().split())
    for i in range(n):
        arr[i] = int(arr[i])
    qi = deque()
    for i in range(k):
        while qi and arr[i] >= arr[qi[-1]]:
            qi.pop()
        qi.append(i)
    for i in range(k,n):
        print(arr[qi[0]],end=' ')
        
        while qi and qi[0] <= i-k:
            qi.popleft()
        while qi and arr[i] >= arr[qi[-1]]:
            qi.pop()
        qi.append(i)
    print(arr[qi[0]])
    t -= 1