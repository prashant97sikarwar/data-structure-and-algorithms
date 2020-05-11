t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    stack = []
    i = 0
    maxarea = -1
    while i < n:
        if (not stack) or arr[stack[-1]] <= arr[i]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            area = arr[top] * ((i - stack[-1] - 1) if (stack) else i)
            maxarea = max(area,maxarea)
    while (stack):
        top = stack.pop()
        area = arr[top] * ((i - stack[-1] - 1) if(stack) else i)
        maxarea = max(area,maxarea)
    print(maxarea)
    t -= 1