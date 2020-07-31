class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        mod = 1000000007
        count = 0
        mark = [True for i in range(n+1)]
        p = 2
        while p*p <= n:
            if mark[p] == True:
                for i in range(p*p,n+1,p):
                    mark[i] = False
            p += 1
        for i in range(2,n+1):
            if mark[i] == True:
                count += 1
        ml = self.fact(count)
        ds = self.fact(n-count)
        ans = ((ml%mod)*(ds%mod))%mod
        return ans
        
    def fact(self,n):
        res = 1
        for i in range(2,n+1):
            res = (res*i)%1000000007
        return res