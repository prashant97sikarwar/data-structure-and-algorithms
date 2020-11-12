#Problem Link ;- https://atcoder.jp/contests/dp/tasks/dp_b

def helper(arr,n,k):
    if (n==2):
        return abs(arr[1]-arr[0])
    dp = [0 for i in range(n)]
    dp[1] = abs(arr[1] - arr[0])
    for i in range(2,n):
        dp[i] = float("inf")
        for k in range(1,k+1):
            if i-k >= 0:
                dp[i] = min(dp[i], dp[i-k] + abs(arr[i] - arr[i-k]))
    return dp[n-1]

n,k = map(int,input().split())
arr = list(map(int,input().split()))
print(helper(arr,n,k))
