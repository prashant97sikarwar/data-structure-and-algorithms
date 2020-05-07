class node:
    def __intit__(self,val):
        self.data = val
        self.left = None
        self.right = None
def height(root):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 1
    else:
        ans = 1 + max(height(root.left),height(root.right))
        return ans
