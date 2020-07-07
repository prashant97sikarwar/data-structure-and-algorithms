class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x:abs(x[0] - x[1]), reverse = True)
        ans = 0
        c1 = 0
        c2 = 0
        i = 0
        n = len(costs)//2
        while i < 2*n:
            if ((costs[i][0] <= costs[i][1]) and (c1 < n)) or (c2 == n):
                ans += costs[i][0]
                i += 1
                c1 += 1
            else:
                ans += costs[i][1]
                i += 1
                c2 += 1
        return ans