t = int(input())
while t > 0:
    s,p = map(str,input().split())
    if len(s) == len(p):
        res = 0
        yo = 0
        for i in range(len(s)):
            res += ord(s[i])
            yo += ord(p[i])
        if res == yo:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
    t -= 1