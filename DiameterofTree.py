# https://practice.geeksforgeeks.org/problems/diameter-of-binary-tree/1
#  in Leetcode ans just do -1 in returned answer.
class Solution:
    #Function to return the diameter of a Binary Tree.
    def __init__(self):
        self.ans = -1
    def height (self, root):
        if root == None:
            return 0
        x = self.height(root.left)
        y = self.height(root.right)
        self.ans = max(self.ans , x+y+1)
        return 1 + max(x , y)
        
    def diameter(self,root):
        # Code here
        self.height(root)
        return self.ans
