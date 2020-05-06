#class node to add new data as a node
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
mn = -10001
mx = 10001
def myfunc(root,mn,mx):
    if root is None:
        return True
    if root.data < mn or root.data > mx:
        return False
    return myfunc(root.left, mn, root.data - 1) and myfunc(root.right, root.data + 1, mx)

def checkBST(root):
    return myfunc(root,mn,mx)

#mn and mx can change according constraint
#or can consider it to be pow(2,32)