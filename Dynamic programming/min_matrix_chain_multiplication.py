def solve(arr,i,j):
    dp = [[-1 for i in range(len(arr))] for i in range(len(arr))]
    mn = float('inf')
    if i >= j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    else:
        for k in range(i,j):
            ans = solve(arr,i,k) + solve(arr,k+1,j) + arr[i-1]*arr[k]*arr[j]
            if ans < mn:
                mn = ans
        dp[i][j] = mn
        return dp[i][j]
       

t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    print(solve(arr,1,n-1))
    t -= 1