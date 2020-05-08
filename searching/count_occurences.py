def countOccurence(arr,n,k):
    l = n/k
    arr.sort()
    count = 1
    flag = 0
    for i in range(1,n):
        if arr[i] != arr[i-1]:
            if count > l:
                flag += 1
            count = 1
        else:
            count += 1
    if count > l:
        flag += 1
    return flag