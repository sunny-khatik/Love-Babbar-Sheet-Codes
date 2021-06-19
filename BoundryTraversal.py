# code library solution
# https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1
class Solution:
    def pleft(self, root,ans):
        if root == None:
            return
        if root.left != None:
            ans.append(root.data)
            self.pleft(root.left,ans)
        elif root.right != None:
            ans.append(root.data)
            self.pleft(root.right,ans)
    def leaf(self, root,ans):
        if root == None:
            return root
        self.leaf(root.left,ans)
        if root.left == None and root.right == None:
            ans.append(root.data)
        self.leaf(root.right,ans)
    def pright(self,root,ans):
        if root == None:
            return
        if root.right != None:
            
            self.pright(root.right,ans)
            ans.append(root.data)
        elif root.left != None:
            
            self.pright(root.left,ans)
            ans.append(root.data)
        
            
    def printBoundaryView(self,root):
        ans= list()
        ans.append(root.data)
        self.pleft(root.left,ans)
        self.leaf(root, ans)
        self.pright(root.right,ans)
        return ans
