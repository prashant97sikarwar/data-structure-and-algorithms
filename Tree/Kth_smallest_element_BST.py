class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
         
         
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        l = [0,0]
        self.inorder(root,l,k)
        return l[1]
        
    def inorder(self,root,l,k):
        if root is None:
            return 
        self.inorder(root.left,l,k)
        l[0] += 1
        if l[0] == k:
            l[1] = root.val
            return 
        self.inorder(root.right,l,k)