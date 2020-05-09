class node:
    def __init__(self, val):
        self.data = val
        self.next = None

def pairwiseSwap(head):
    if head is not None and head.next is not None:
        head.data,head.next.data = head.next.data,head.data
        pairwiseSwap(head.next.next)
        return head