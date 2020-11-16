#Problem Link:- https://atcoder.jp/contests/dp/tasks/dp_c

n = int(input())
mat = []
for i in range(n):
    arr = list(map(int,input().split()))
    mat.append(arr)
dp = [[0 for i in range(3)] for i in range(n)]
for i in range(3):
    dp[n-1][i] = mat[n-1][i]
for i in range(n-2,-1,-1):
    for j in range(3):
        dp[i][j] = mat[i][j]
        if j == 0:
            dp[i][j] += max(dp[i+1][j+1],dp[i+1][j+2])
        elif j == 2:
            dp[i][j] += max(dp[i+1][j-1],dp[i+1][j-2])
        else:
            dp[i][j] += max(dp[i+1][j-1],dp[i+1][j+1])
mx = 0
for i in range(3):
    mx = max(mx,dp[0][i])
print(mx)