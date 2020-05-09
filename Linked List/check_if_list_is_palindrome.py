class node:
    def __init__(self,val):
        self.next = None
        self.data = val

def isPalindrome(head):
    l = []
    curr = head
    while curr is not None:
        l.append(curr.data)
        curr = curr.next
    yo = l[::-1]
    if yo == l:
        return True
    else:
        return False