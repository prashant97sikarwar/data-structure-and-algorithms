class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
def getMaxWidth(root):
    if root is None:
        return 1
    que = []
    que.append(root)
    ans = 1
    while que:
        count = len(que)
        while count > 0:
            curr = que.pop(0)
            if curr.left:
                que.append(curr.left)
            if curr.right:
                que.append(curr.right)
            count -= 1 
        d = len(que)
        ans = max(d,ans)
    return ans
