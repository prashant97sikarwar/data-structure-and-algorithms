class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


def postOrder(root):
    if root is None:
        return -1
    else:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data,end=' ')