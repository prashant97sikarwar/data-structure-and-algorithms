class node:
    def __init__(self,val):
        self.next = None
        self.data = val
def intersetPoint(head_a,head_b):
    curr = head_a
    purr = head_b
    while curr is not None:
        curr.data = curr.data - 1001
        curr = curr.next
    ans = -1
    while purr is not None:
        if purr.data >= 0:
            purr = purr.next
        else:
            purr.data = purr.data + 1001
            ans = purr
            break
    return ans