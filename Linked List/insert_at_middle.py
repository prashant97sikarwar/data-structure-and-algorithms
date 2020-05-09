class Node:
    def __init__(self,val):
        self.next = None
        self.data = val
        
def insertInMid(head,node):
    p = head
    x = head
    while x.next is not None and x.next.next is not None:
        p = p.next
        x = x.next.next
    temp = p.next
    p.next = node
    node.next = temp
    return
