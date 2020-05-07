class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None


def rightView(root):
    if root is None:
        return
    que = []
    que.append(root)
    while que:
        count = len(que)
        while count > 0:
            curr = que[0]
            que.pop(0)
            if curr.left is not None:
                que.append(curr.left)
            if curr.right is not None:
                que.append(curr.right)
            count -= 1
        print(curr.data,end=' ')
