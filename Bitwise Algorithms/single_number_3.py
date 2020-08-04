class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for i in nums:
            xor ^= i
        xor = xor & (~xor + 1)
        
        a,b = 0,0
        for n in nums:
            if n & xor:
                a ^= n
            else:
                b ^= n
        return [a,b]