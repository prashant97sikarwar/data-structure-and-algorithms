class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pos, neg = set(), set()
        result = set()
        d = {}
        for num in nums:
            d.setdefault(num, 0)
            d[num] += 1
            if num > 0:
                pos.add(num)
            elif num < 0:
                neg.add(num)
        if d.get(0, 0) >= 3:
            result.add((0, 0, 0))
        for x in pos:
            d[x] -= 1
            for y in neg:
                d[y] -= 1
                z = -x - y
                if z in d and d[z] > 0:
                    result.add(tuple(sorted((x, y, z))))
                d[y] += 1
            d[x] += 1
            
        return list(result)