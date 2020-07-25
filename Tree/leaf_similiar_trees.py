 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaves1 = []
        leaves2 = []
        self.myfun(root1,leaves1)
        self.myfun(root2,leaves2)
        if leaves1 == leaves2:
            return True
        else:
            return False
    def myfun(self,root,leaves):
        if root:
            if root.left is None and root.right is None:
                leaves.append(root.val)
            self.myfun(root.left,leaves)
            self.myfun(root.right,leaves)