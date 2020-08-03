class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        l = nums[0]
        for i in nums:
            l = gcd(l,i)
        if l == 1:
            return True
        return False
        
    def gcd(self,a,b):
        if a == 0:
            return b
        else:
            return self.gcd(b,a%b)
        