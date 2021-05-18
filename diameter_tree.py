import sys
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return self.diameter(root)-1
    def diameter(self , root):
        if root is None:
            return 0
 
        lheight = self.height(root.left)
        rheight = self.height(root.right)
        
        ldiameter = self.diameter(root.left)
        rdiameter = self.diameter(root.right)
        
        return max(lheight + rheight + 1, max(ldiameter, rdiameter))
    
    def height(self,node):
        if node is None:
            return 0
        return 1+max(self.height(node.left), self.height(node.right))
