class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None

def levelOrder(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while queue:
        count = len(queue)
        while count > 0:
            curr = queue.pop(0)
            print(curr.data,end=' ')
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
            count -= 1
        
        print('$',end=' ')