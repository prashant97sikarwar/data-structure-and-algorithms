class Node:

	def __init__(self, data):
		self.data = data
		self.next = None


class Stack:
    def __init__(self):
        self.head = None
        
    def push(self, data):
        if self.head == None:
            newnode = Node(data)
            self.head = newnode
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def pop(self):
        if self.head == None:
            return -1
        else:
            xp = self.head
            self.head = self.head.next
            xp.next = None
            return xp.data

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = Stack()
        q = int(input())
        q1 = list(map(int, input().split()))
        i = 0
        while(i < len(q1)):
            if(q1[i] == 1):
                s.push(q1[i + 1])
                i = i + 2
            elif(q1[i] == 2):
                print(s.pop(), end=" ")
                i = i + 1
            elif(s.isEmpty()):
                print(-1)
        print()
