import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

def solve(arr,n):
    dp = [1 for i in range(n)]
    for i in range(1,n):
        for j in range(i):
            if (abs(arr[i]) > abs(arr[j])) and ((arr[i] > 0 and arr[j] < 0) or (arr[j] > 0 and arr[i] < 0)):
                dp[i] = max(dp[i],1+dp[j])
    return dp[n-1]

n = inp()
arr = inlt()
print(solve(arr,n))