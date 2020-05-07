class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None

def isSumProperty(node):
    left_data = 0
    right_data = 0
    if(node == None or (node.left == None and 
                        node.right == None)):  
        return 1
    else: 
        if(node.left != None): 
            left_data = node.left.data  
        if(node.right != None): 
            right_data = node.right.data  
        if((node.data == left_data + right_data) and 
                        isSumProperty(node.left) and 
                        isSumProperty(node.right)): 
            return 1
        else: 
            return 0
  