# code library
# https://practice.geeksforgeeks.org/problems/binary-tree-to-dll/1
class Test:
    def __init__(self):
        self.flag = 0
        self.prev = self.head = None
        
    def inorder(self,root):
        if root == None:
            return
        self.inorder(root.left)
        if self.flag == 0:
            self.flag = 1
            self.head = root
            self.prev = root
            
        else:
            self.prev.right = root
            self.prev.right.left = self.prev
            self.prev = self.prev.right
        self.inorder(root.right)
        return self.head
        
def bToDLL(root):
    o = Test()
    head = o.inorder(root)
    return head
