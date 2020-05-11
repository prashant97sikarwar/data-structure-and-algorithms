t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    stack = list()
    flag = []
    for i in range(n-1,-1,-1):
        while (len(stack) > 0 and arr[i] >= stack[-1]):
            stack.pop()
        if len(stack) == 0:
            flag.append(-1)
        else:
            flag.append(stack[-1])
        stack.append(arr[i])
    for i in range(n-1,-1,-1):
        print(flag[i],end=' ')
    print()
    t -= 1