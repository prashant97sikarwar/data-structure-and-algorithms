def majorityWins(arr, n,  x,y):
    c = 0
    d = 0
    for i in range(n):
        if arr[i] == x:
            c += 1
        elif arr[i] == y:
            d += 1
    if c == d:
        ans = x if x < y else y 
    elif c > d:
        ans = x
    else:
        ans = y
    return ans