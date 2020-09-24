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


def LongestBitonicSequence(arr):
    n = len(arr)
    dp = [1 for i in range(n)]
    for i in range(1,n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i],1 + dp[j])
    ddp = [1 for i in range(n)]
    for i in range(n-2,-1,-1):
        for j in range(n-1,i,-1):
            if arr[i] > arr[j]:
                ddp[i] = max(ddp[i],1 + ddp[j])
    mx = dp[0] + ddp[0] - 1
    for i in range(1,n):
        mx = max(mx,dp[i] + ddp[i] - 1)
    return mx

t = inp()
while t > 0:
    arr = inlt()
    n = len(arr)
    print(LongestBitonicSequence(arr))
    t -= 1