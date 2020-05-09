def segregate(head):
    zerod = Node(0)
    oned = Node(0)
    twod = Node(0)
    
    zero = zerod
    one = oned
    two = twod
    
    curr = head
    while curr is not None:
        if curr.data == 0:
            zero.next = curr
            zero = zero.next
            curr = curr.next
        elif curr.data == 1:
            one.next = curr
            one = one.next
            curr = curr.next
        else:
            two.next = curr
            two = two.next
            curr = curr.next
    zero.next = oned.next if (oned.next) else twod.next
    one.next = twod.next
    two.next = None
    
    head = zerod.next
    return head