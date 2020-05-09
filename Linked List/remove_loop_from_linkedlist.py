class node:
    def __init__(self,val):
        self.next = None
        self.data = val
        
def removeTheLoop(head):
    slow_p = fast_p = head 
    while(slow_p and fast_p and fast_p.next): 
        slow_p = slow_p.next
        fast_p = fast_p.next.next
        if slow_p == fast_p: 
            removeLoop(head,slow_p)  
            return 1
    return 0 
def removeLoop(head, loop_node): 
    ptr1 = loop_node 
    ptr2 = loop_node 
    k = 1 
    while(ptr1.next != ptr2): 
        ptr1 = ptr1.next
        k += 1
 
    ptr1 = head 
    ptr2 = head 
    for i in range(k): 
        ptr2 = ptr2.next
    while(ptr2 != ptr1): 
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    while(ptr2.next != ptr1): 
        ptr2 = ptr2.next
  
    ptr2.next = None
    