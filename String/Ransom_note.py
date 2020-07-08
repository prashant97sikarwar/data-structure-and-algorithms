class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1 = dict()
        d2 = dict()
        for i in ransomNote:
            if i not in d1:
                d1[i] = 1
                d2[i] = 0
            else:
                d1[i] += 1
        for i in magazine:
            if i not in d2:
                d2[i] = 1
                if i not in d1:
                    d1[i] = 0
            else:
                d2[i] += 1
        for i in ransomNote:
            if d1[i] > d2[i]:
                return False
        return True