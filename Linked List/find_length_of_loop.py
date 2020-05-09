class node:
    def __init__(self,val):
        self.next = None
        self.data = val

        
def countNodesinLoop(head):
    p = head
    x = head
    flag = 0
    while p.next is not None and p.next.next is not None:
        if p == x and flag != 0:
            count = 1
            p = p.next
            while p != x:
                p = p.next
                count += 1
            return count
        else:
            flag = 1
            p = p.next.next
            x = x.next
            
    return 0
