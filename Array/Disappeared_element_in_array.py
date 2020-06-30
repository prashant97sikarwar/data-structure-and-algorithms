class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l =  []
        n = len(nums) + 1
        for i in range(len(nums)):
            nums[(nums[i] % n)-1] += n 
        for i in range(len(nums)):
            nums[i] = int(nums[i]/n)
        for i in range(len(nums)):
            if nums[i] == 0:
                l.append(i+1)
        return l