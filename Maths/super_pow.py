class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        num = 0
        for i in b:
            num = 10*num  + i
        p = 1337
        return self.power(a,num,p)
    def power(self,a,num,p):
        if num == 0:
            return 1
        if num % 2 == 0:
            return self.power((a*a)%p,num//2,p)
        if num % 2 == 1:
            return (a * self.power((a*a)%p,num//2,p))%p
   