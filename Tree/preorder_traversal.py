class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None

def PreOrder(root):
    if root is None:
        return -1
    else:
        print(root.data,end=' ')
        PreOrder(root.left)
        PreOrder(root.right)
