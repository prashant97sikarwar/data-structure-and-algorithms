def subsetDiff(arr,n,sm):
    dp = [[False for i in range(sm+1)] for j in range(n+1)]
    dp[0][0] = True
    for i in range(1,n+1):
        dp[i][0] = True
    for i in range(1,n+1):
        for j in range(1,sm+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][sm]

t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    sm = 0
    for i in range(n):
        sm += arr[i]
    print(subsetDiff(arr,n,sm))
    t -= 1