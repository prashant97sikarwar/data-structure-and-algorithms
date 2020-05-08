def countingSort(s,n):
    l = 26
    arr = [0]*l
    for i in range(n):
        arr[ord(s[i]) - ord('a')] += 1
    for i in range(26):
        for j in range(arr[i]):
            print(chr(ord('a') + i),end='')
