class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Height:
    def __init__(self):
        self.h = 0

def another(root, height):
    lh = Height()
    rh = Height()
    
    if root is None:
        height.h = 0
        return 0
    ldiameter = another(root.left,lh)
    rdiameter = another(root.right,rh)
    
    height.h = 1 + max(lh.h,rh.h)
    
    return max(lh.h + rh.h + 1, max(ldiameter, rdiameter))
    
def diameter(root):
    height = Height()
    return another(root, height)

