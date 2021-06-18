# important because of global variable is not there
# see code library for explanation
# https://practice.geeksforgeeks.org/problems/check-for-balanced-tree/1
def solve(root):
    if root == None:
        return True,0
    bal,l_h = solve(root.left)
    if not bal:
        return False , 0
    bal,r_h = solve(root.right)
    if not bal:
        return False , 0
    if abs(l_h-r_h) > 1:
        return False,0
    return True,1+max(l_h,r_h)
        
#Function to check whether a binary tree is balanced or not.
def isBalanced(root):
    res,_ = solve(root)
    return res
