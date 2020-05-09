def sumExists(arr,sizeOfArray,sum):
    arr.sort()
    i = 0
    j = sizeOfArray - 1
    ans = 0
    while i < j:
        if arr[i] + arr[j] == sum:
            ans = 1
            break
        elif arr[i] + arr[j] > sum:
            j -= 1
        else:
            i += 1
    return ans    
    