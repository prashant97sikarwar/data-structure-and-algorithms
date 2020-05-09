def strstr(s,p):
    flag = 0
    for i in range(len(s)):
        if s[i:i+len(p)] == p:
            flag = 1
            return i
    if flag == 0:
        return -1