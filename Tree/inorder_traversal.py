class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None

def InOrder(root):
    if root is None:
        return -1
    else:
        InOrder(root.left)
        print(root.data,end=' ')
        InOrder(root.right)