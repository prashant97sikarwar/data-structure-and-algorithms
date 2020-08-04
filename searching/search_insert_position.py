class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r  = len(nums) - 1
        return self.bsearch(nums,l,r,target)
        
        
    def bsearch(self,nums,l,r,target):
        if l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return self.bsearch(nums,mid+1,r,target)
            else:
                return self.bsearch(nums,l,mid-1,target)
        else:
            return r +1
                
            
    
    