"""return total number of ways to change given total, with the 
infinite supply of given coins"""

import math
import os
import random
import re
import sys

def getWays(n, c):
    ln = len(c)
    dp = [[0 for i in range(n+1)] for j in range(ln+1)]
    dp[0][0] = 1
    for i in range(1,ln+1):
        dp[i][0] = 1
    for i in range(1,ln+1):
        for j in range(n+1):
            if c[i-1] <= n:
                dp[i][j] = dp[i][j-c[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[ln][n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))
    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
