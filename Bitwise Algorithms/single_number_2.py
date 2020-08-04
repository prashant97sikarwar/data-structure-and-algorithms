class Solution:
    def singleNumber(self,nums):
        x = 1
        res = 0
        for i in range(32):
            count = 0
            for j in range(len(nums)):
                if (x << i) & nums[j] == 1<<i:
                    count += 1
            res |= (count%3) << i
        return res if res < (1<<31) else res - (1<<32)
