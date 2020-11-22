class Solution:
    def findJudge(self, N,trust):
        if len(trust) < N-1:
            return -1
        s = [0] * (N+1)
        for i,j in trust:
                s[i] -= 1
                s[j] += 1
        for i in range(1,N+1):
            if s[i] == N-1:
                return i
        return -1

