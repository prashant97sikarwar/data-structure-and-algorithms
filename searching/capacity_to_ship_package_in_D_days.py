class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = left + (right-left)//2
            if self.check(mid,weights,D):
                right = mid
            else:
                left = mid + 1
        return left
        
            
            
    def check(self,capacity,weights,D):
        days = 1
        total = 0
        for wt in weights:
            total += wt
            if total > capacity:
                days += 1
                total = wt
                if days > D:
                    return False
        return True
    