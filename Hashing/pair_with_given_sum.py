def sumExists(arr,sizeOfArray,sum):
    s = set()
    for i in range(sizeOfArray):
        s.add(arr[i])
    flag = 0
    for i in range(sizeOfArray):
        if ((sum - arr[i]) in s) and 2*arr[i] != sum:
            flag = 1
            break
    if flag == 1:
        return 1
    else:
        return 0
            