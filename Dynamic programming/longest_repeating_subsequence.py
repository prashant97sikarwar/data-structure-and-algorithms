def lengthSub(str1,str2,n):
    dp = [[0 for i in range(n+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            if  i == 0 or j == 0:
                dp[i][j] = 0
            elif str1[i-1] == str2[j-1] and i != j:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][n]


t = int(input())
while t > 0:
    n = int(input())
    str1 = input()
    print(lengthSub(str1,str1,n))
    t -= 1