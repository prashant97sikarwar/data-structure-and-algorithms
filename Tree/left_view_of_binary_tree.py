class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None


def LeftView(root):
    if root is None:
        return
    que = []
    que.append(root)
    while que:
        count = len(que)
        l = 0
        while count > 0:
            curr = que[0]
            l += 1
            if l == 1:
                print(curr.data,end=' ')
            que.pop(0)
            if curr.left is not None:
                que.append(curr.left)
            if curr.right is not None:
                que.append(curr.right)
            count -= 1
    