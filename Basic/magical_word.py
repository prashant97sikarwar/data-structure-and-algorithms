    from sys import *
    def isPrime(n) : 
     
        if (n <= 1) : 
            return False
        if (n <= 3) : 
            return True
      
        if (n % 2 == 0 or n % 3 == 0) : 
            return False
      
        i = 5
        while(i * i <= n) : 
            if (n % i == 0 or n % (i + 2) == 0) : 
                return False
            i = i + 6
      
        return True
    t = int(stdin.readline())
    while t > 0:
        n = int(stdin.readline())
        s = stdin.readline().strip()
        l = []
        for i in range(ord('a'),ord('z')+1):
            if isPrime(i):
                l.append(chr(i))
        for i in range(ord('A'),ord('Z')+1):
            if isPrime(i):
                l.append(chr(i))
        s = list(s)
        for i in range(len(s)):
            if isPrime(ord(s[i])):
                continue
            else:
                mn = 345
                for j in l:
                    des = abs(ord(s[i]) - ord(j))
                    if des < mn:
                        mn = des
                        ind = j
                s[i] = ind
        for i in range(len(s)):
            if s[i] == '5' or s[i] == 5:
                s[i] = 'C'
        ans = ''.join(s)
        if len(ans) == n:
            print(ans)
        else:
            ans = ans[:n]
            print(ans)
        t -= 1
        