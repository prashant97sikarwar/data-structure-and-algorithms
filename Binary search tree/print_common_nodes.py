class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def inorder(root,l1):
    if root is None:
        return
    inorder(root.left,l1)
    l1.append(root.data)
    inorder(root.right,l1)
    
    
def printCommon(root1, root2):
    if root1 is None:
        return
    if root2 is None:
        return
    l1 =[]
    l2 =  []
    l1 = inorder(root1,l1)
    l2 = inorder(root2,l2)
    s = set()
    for i in range(len(l1)):
        if l1[i] not in s:
            s.add(l1[i])
    ans = []
    for i in range(len(l2)):
        if l2[i] in s:
            ans.append(l2[i])
    return ans