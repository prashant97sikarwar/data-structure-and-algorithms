class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        else:
            ans = 0
            leftsum = sum - root.val
            if leftsum == 0 and root.left is None and root.right is None:
                return True
            if root.left is not None:
                ans = ans or self.hasPathSum(root.left,leftsum)
            if root.right is not None:
                ans = ans or self.hasPathSum(root.right,leftsum)
            return ans 