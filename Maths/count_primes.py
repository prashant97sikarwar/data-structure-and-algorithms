class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        mark = [True for i in range(n+1)]
        p = 2
        while p*p <=n:
            if mark[p] == True:
                for i in range(p*p,n+1,p):
                    mark[i] = False
            p+=1
        for i in range(2,n):
            if mark[i] == True:
                count += 1
        return count