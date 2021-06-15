# https://practice.geeksforgeeks.org/problems/height-of-binary-tree/1
class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
        if root == None:
            return 0
        lhight = self.height(root.left)
        rhight = self.height(root.right)
        if lhight > rhight:
            return lhight+1
            
        else:
            return rhight+1
