def levelOrder( root ):
    if root is None:
        return
    queue = []
    queue.append(root)
    while len(queue) > 0:
        print(queue[0].data,end=' ')
        curr = queue.pop(0)
        if curr.left is not None:
            queue.append(curr.left)
        if curr.right is not None:
            queue.append(curr.right)