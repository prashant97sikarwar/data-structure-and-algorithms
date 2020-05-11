class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    def __init__(self):
        self.head = None
    
    def push(self, item): 
        newnode = Node(item)
        if self.head is None:
            self.head = newnode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newnode

    def pop(self):
        if self.head is None:
            return -1
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            return temp.data