def solve(n,W,arr,ind): 
    dp = [[0 for i in range(W+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,W+1):
            if arr[i-1] <= j:
                dp[i][j] = max(ind[i-1] + dp[i][j-arr[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][W]

t = int(input())
while t > 0:
    n,W = map(int,input().split())
    ind = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    print(solve(n,W,arr,ind))
    t -= 1