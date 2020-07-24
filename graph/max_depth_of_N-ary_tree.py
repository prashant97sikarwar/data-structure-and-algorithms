'''solution based on BFS algorithm'''

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            res = 0
        else:
            res = 0
            que = [root]
            while que:
                dep = []
                for i in que:
                    if i.children:
                        for j in i.children:
                            dep.append(j)
                que =  dep
                res += 1
        return res
    
'''solution based on DFS algorithm'''

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        res = 0
        for child in root.children:
            res = max(res,self.maxDepth(child))
        return res + 1
    
            