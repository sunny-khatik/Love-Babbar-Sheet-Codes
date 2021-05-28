# https://www.geeksforgeeks.org/convert-bst-min-heap/
class Node:
    def __init__ (self,data):
        self.val=data
        self.left=None
        self.right=None
        
        
def inorder(root,arr):
    if root == None:
        return 
    inorder(root.left,arr)
    arr.append(root.val)
    inorder(root.right,arr)
    
    
def bsttominh(root,arr,i):
    if root == None:
        return
    i[0]+=1
    root.val=arr[i[0]]
    bsttominh(root.left,arr,i)
    bsttominh(root.right,arr,i)
    
    
def preorder(root):
    if root == None:
        return 
    print(root.val)
    preorder(root.left)
    preorder(root.right)
    
    
if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)
    arr=list() # we do inorder trversal in binay tree
    # we get sorted output in arr but tree stil in bst
    inorder(root,arr)
    i=[-1]
    # so will use bst to min heap and i=[-1] value so it will becom 0 , 1 , 2  upto...n-1
    # it will store the data into tree 
    # then will traverse preorder so will get a sorted output.
    bsttominh(root,arr,i)
    preorder(root)
