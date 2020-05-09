class node:
    def __init__(self,val):
        self.next = None
        self.data = val

def rotateList(head, k):
    curr = head
    while curr.next is not None:
        curr = curr.next
    for i in range(k):
        temp = head
        curr.next = temp
        head = temp.next
        temp.next = None
        curr = curr.next
    return head