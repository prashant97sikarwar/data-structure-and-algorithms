# Definition for a binary tree node.
 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        parent = {}
        depth = {}
        q = []
        q.append(root)
        parent[root.val] = 0
        depth[root.val] = 0
        while len(q) > 0:
            f = q.pop(0)
            if f.left:
                q.append(f.left)
                parent[f.left.val] = f.val
                depth[f.left.val] = depth[f.val] + 1
            if f.right:
                q.append(f.right)
                parent[f.right.val] = f.val
                depth[f.right.val] =  depth[f.val] + 1
        if depth[x] == depth[y] and parent[x] != parent[y]:
            return True
        else:
            False
            
                