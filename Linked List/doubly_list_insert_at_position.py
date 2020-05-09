class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None


def addNode(head, p, data):
    curr = head
    data = Node(data)
    x = 0
    if head.next is not None:
        while x < p :
            x += 1
            curr = curr.next
        if curr.next is not None:
            temp = curr.next
            curr.next = data
            temp.prev = data
            data.next = temp
            data.prev = curr
        else:
            curr.next = data
            data.prev = curr
    else:
        curr.next = data
        data.prev = curr
    return 
    