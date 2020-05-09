def getCount(head_node):
    count = 0
    curr = head_node
    while curr is not None:
        count += 1
        curr = curr.next
    return count
    