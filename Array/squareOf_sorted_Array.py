class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        l = []
        i = 0
        j = len(A) - 1
        while i <= j:
            if abs(A[i]) >= abs(A[j]):
                l.insert(0,A[i] * A[i])
                i += 1
            else:
                l.insert(0,A[j] * A[j])
                j -= 1
        return l
    