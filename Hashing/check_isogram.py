t = int(input())
while t > 0:
    s = input()
    arr = [0]*26
    for i in range(len(s)):
        arr[ord(s[i]) - ord('a')] += 1
    flag = 0
    for i in range(26):
        if arr[i] > 1:
            flag = 1
            break
    if flag == 0:
        ans = 1
    else:
        ans = 0
    print(ans)
    t -= 1