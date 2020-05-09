class node:
    def __init__(self, val):
        self.data = val
        self.next = None


def areIdentical(head1, head2):
    curr = head1
    purr = head2
    flag = 0
    x =  1
    y = 1
    while curr.next is not None:
        x +=  1
        curr = curr.next
    while purr.next is not None:
        y += 1
        purr = purr.next
    if x == y:
        mes = head1
        pes = head2
        if mes.data == pes.data:
            while mes.next is not None and pes.next is not None:
                mes = mes.next
                pes = pes.next
                if mes.data != pes.data:
                    flag = 1
                    break
        else:
            flag = 1
    else:
        flag = 1
    if flag == 0:
        return True
    else:
        return False
        