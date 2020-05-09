class node:
    def __init__(self,val):
        self.next = None
        self.data = val

def deleteNode(curr_node):
    temp = curr_node.next
    curr_node.data = temp.data
    curr_node.next = temp.next
    return
    