class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        d = {}
        count = 0
        for i in A:
            for j in B:
                df = i + j
                if df not in d:
                    d[df] = 1
                else:
                    d[df] += 1
        for i in C:
            for j in D:
                tar = 0 - (i+j)
                if tar in d:
                    count += d[tar]
        return count