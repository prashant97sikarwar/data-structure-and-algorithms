class node:
    def __init__(self,val):
        self.next = None
        self.data = val
        
def removeDuplicates(head):
    if head == None:
        return
    if head.next != None:
        if head.data == head.next.data:
            head.next = head.next.next
            removeDuplicates(head)
        else:
            removeDuplicates(head.next)
    return 
        