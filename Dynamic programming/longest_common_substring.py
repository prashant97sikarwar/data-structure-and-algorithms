def longestCommonSubstring(n,m,X,Y):
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    result = 0
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif X[i-1] == Y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                result = max(result,dp[i][j])
            else:
                dp[i][j] = 0
    return result

t = int(input())
while t > 0:
    n,m = map(int,input().split())
    X = input()
    Y = input()
    print(longestCommonSubstring(n,m,X,Y))
    t -= 1