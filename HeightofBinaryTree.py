# https://practice.geeksforgeeks.org/problems/height-of-binary-tree/1
class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
        if root == None:
            return 0
        return 1 + max(self.height(root.left) ,self.height(root.right))
