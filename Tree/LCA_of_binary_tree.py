class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

def lca(root, n1, n2):
    if root is None:
        return None
    if root.data == n1 or root.data == n2:
        return root
    left_lca  = lca(root.left,n1,n2)
    right_lca = lca(root.right,n1,n2)
    if left_lca and right_lca:
         return root
    return left_lca if left_lca else right_lca    
