def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left),height(root.right))
    
def isBalanced(root):
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    
    if abs(lh - rh) <= 1 and isBalanced(root.left) and isBalanced(root.right):
        return True
    return False