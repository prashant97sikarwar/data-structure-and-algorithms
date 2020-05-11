def solution(arr,n):
    stack = []
    right = [n] * (n+1)
    left = [-1] * (n+1)
    for i in range(n): 
        while (len(stack) != 0 and 
               arr[stack[-1]] >= arr[i]):  
            stack.pop()  
  
        if (len(stack) != 0): 
            left[i] = stack[-1] 
  
        stack.append(i)
    while (len(stack) != 0): 
        stack.pop() 
    for i in range(n - 1, -1, -1): 
        while (len(stack) != 0 and arr[stack[-1]] >= arr[i]):  
            stack.pop()  
  
        if(len(stack) != 0):  
            right[i] = stack[-1]  
  
        stack.append(i) 
    ans = [0] * (n+1)
    for i in range(n):
        f = right[i] - left[i] - 1
        ans[f] = max(arr[i],ans[f])
    for i in range(n-1,0,-1):
        ans[i] = max(ans[i],ans[i+1])
    for i in range(1,n+1):
        print(ans[i],end=' ')
        
t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    solution(arr,n)
    print()
    t-=1
    