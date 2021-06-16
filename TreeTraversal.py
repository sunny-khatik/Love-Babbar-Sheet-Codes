# Inorder preorder postorder
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
# def printPostorder(root):
#     if root == None:
#         return
#     ans = list()
#     stack = list()
#     stack.append(root)
#     while len(stack) > 0:
#         node = stack.pop()
#         ans.append(node.data)
#         if node.left:
#             stack.append(node.left)
#         if node.right:
#             stack.append(node.right)
#     while ans:
#         print(ans.pop(),end=" ")
# def printInorder(root):
#     if root == None:
#         return
#     stack = list()
#     while len(stack) > 0 or root != None:
#         if root:
#             stack.append(root)
#             root=root.left
#         else:
#             root = stack.pop(-1)
#             print(root.data,end=" ")
#             root = root.right
    
# def printPreorder(root):
#     if root == None:
#         return
#     stack = list()
#     stack.append(root)
#     while len(stack) > 0:
#         node = stack.pop()
#         print(node.data , end=" ")
#         if node.right != None:
#             stack.append(node.right)
#         if node.left != None:
#             stack.append(node.left)     
def printPostorder(root):
    if root != None:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.data, end=" ")
    else:
        return
def printInorder(root):
    if root != None:
        printInorder(root.left)
        print(root.data, end=" ")
        printInorder(root.right)
    else:
        return

def printPreorder(root):
    if root != None:
        print(root.data, end=" ")
        printPreorder(root.left)
        
        printPreorder(root.right)
    else:
        return

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
#            1
#      2          3
# 4       5   N       N
print ("Preorder traversal of binary tree is")
printPreorder(root)
 
print( "\nInorder traversal of binary tree is")
printInorder(root)
 
print( "\nPostorder traversal of binary tree is")
printPostorder(root)]

# output
# Preorder traversal of binary tree is

# 1 2 4 5 3 

# Inorder traversal of binary tree is

# 4 2 5 1 3 

# Postorder traversal of binary tree is

# 4 5 2 3 1 


