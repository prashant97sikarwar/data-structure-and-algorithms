class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        le = set(J)
        count = 0
        for i in S:
            if i in le:
                count += 1
        return count