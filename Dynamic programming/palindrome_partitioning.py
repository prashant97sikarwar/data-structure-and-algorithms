def isPal(s,i,j):
    while i < j:
        if s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1
    return True

def solve(s,i,j,dp):
    if i >= j:
        return 0
    if isPal(s,i,j):
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    mn = float('inf')
    for k in range(i,j):
        cur = 1 + solve(s,i,k,dp) + solve(s,k+1,j,dp)
        mn = min(cur,mn)
    dp[i][j] = mn
    return dp[i][j]
    
t = int(input())
while t > 0:
    s = input()
    dp = [[-1 for i in range(1001)] for j in range(1001)]
    print(solve(s,0,len(s)-1,dp))
    t -= 1