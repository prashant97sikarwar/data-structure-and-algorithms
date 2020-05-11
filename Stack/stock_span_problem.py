t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    stack = list()
    flag = [0 for i in range(n)]
    flag[0] = 1
    stack.append(0)
    for i in range(1,n):
        while (len(stack) > 0 and arr[stack[-1]] <= arr[i]):
            stack.pop()
        flag[i] = i+1 if len(stack) <= 0 else (i - stack[-1])
        stack.append(i)
    for i in range(n):
        print(flag[i],end=' ')
    print()
    t -= 1
            