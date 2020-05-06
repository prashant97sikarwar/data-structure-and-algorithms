def threeWayPartition(arr, n, a, b):
    l = []
    m = []
    r = []
    for i in range(n):
        if arr[i] < a:
            l.append(arr[i])
        elif arr[i] >= a and arr[i] <= b:
            m.append(arr[i])
        else:
            r.append(arr[i])
    ans = l + m + r
    return ans
            