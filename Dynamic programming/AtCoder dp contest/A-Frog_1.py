#Problem Link :- https://atcoder.jp/contests/dp/tasks/dp_a

def helper(arr,n):
    if n == 2:
        return abs(arr[1] - arr[0])
    dp = [0 for i in range(n)]
    dp[1] = abs(arr[1] - arr[0])
    for i in range(2,n):
        dp[i] = min(dp[i-2]+abs(arr[i]-arr[i-2]), dp[i-1] + abs(arr[i] - arr[i-1]))
    return dp[n-1]

n = int(input())
arr = list(map(int,input().split()))
print(helper(arr,n))