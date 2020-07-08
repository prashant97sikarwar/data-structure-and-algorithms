class Solution:
    import math
    def findComplement(self, num: int) -> int:
        if num < 0:
            return -num
        elif num == 1 or num == 0:
            return 0
        else:
            dep = math.log(num,2)
            po = int(math.floor(dep) + 1)
            ans = ((1 << po) -1) ^ num
            return ans