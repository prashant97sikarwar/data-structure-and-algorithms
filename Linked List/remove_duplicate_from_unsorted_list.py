class node:
    def __init__(self,val):
        self.next = None
        self.data = val
        

def removeDuplicates(head):
    s = set()
    cur = head
    while cur.next is not None:
        s.add(cur.data)
        if cur.next.data in s:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head