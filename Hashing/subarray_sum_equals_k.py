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


def subarraySum(nums, k):
    res =0 
    d = dict()
    sm = 0
    d[0] = 1
    for i in range(len(nums)):
        sm += nums[i]
        if sm-k in d:
            res += d[sm-k]
        if sm in d:
            d[sm] += 1
        else:
            d[sm] = 1
    return res 


t = inp()
while t > 0:
    n = inp()
    arr = inlt()
    print(subarraySum(arr,k))
    t -= 1