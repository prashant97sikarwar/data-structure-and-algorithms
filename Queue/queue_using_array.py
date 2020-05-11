class MyQueue:
    def __init__(self):
        self.arr = []
        
    
    
    def push(self, item):
        self.arr.append(item)
     
    def pop(self): 
        if len(self.arr) == 0:
            return -1
        else:
            ans = self.arr.pop(0)
            return ans

