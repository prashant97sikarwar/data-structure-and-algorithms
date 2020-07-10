class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) -1
        while low  <= high:
            mid = low + (high-low)//2
            if low == high:
                ans  = nums[low]
                break
            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    low = mid + 2
                else:
                    high = mid
            else:
                if nums[mid] == nums[mid - 1]:
                    low = mid + 1
                else:
                    high = mid - 1
        return ans 
    