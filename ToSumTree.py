#code library
# https://practice.geeksforgeeks.org/problems/transform-to-sum-tree/1
class Solution:
    def toSumTree(self, root) :
        #code here
        if root == None:
            return 0
        x = self.toSumTree(root.left)
        y = self.toSumTree(root.right)
        z = root.data
        root.data = x+y
        return x+y+z
