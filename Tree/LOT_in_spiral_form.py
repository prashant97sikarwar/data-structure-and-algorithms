class Node:
    def init(self, val):
        self.right = None
        self.data = val
        self.left = None

def printSpiral(root):
    if root is None:
        return
    st1 = []
    st2 = []
    st1.append(root)
    while st1 or st2:
        while st1:
            temp = st1[-1]
            st1.pop()
            print(temp.data,end=' ')
            if temp.right is not None:
                st2.append(temp.right)
            if temp.left is not None:
                st2.append(temp.left)
        while st2:
            temp = st2[-1]
            st2.pop()
            print(temp.data,end=' ')
            if temp.left is not None:
                st1.append(temp.left)
            if temp.right is not None:
                st1.append(temp.right)
        