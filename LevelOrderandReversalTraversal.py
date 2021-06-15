# https://practice.geeksforgeeks.org/problems/reverse-level-order-traversal/1
# https://practice.geeksforgeeks.org/problems/level-order-traversal/1#
class Solution:
    #Function to return the level order traversal of a tree.
    def solve(self,root,l):
        if root == None:
            l.append("N")
            return 
        queue = list()
        queue.append(root)
        while len(queue) > 0:
            l.append(queue[0].data)
            node = queue.pop(0)
            
            if node.right != None:
                queue.append(node.right)
            if node.left != None:
                queue.append(node.left)
                
    def levelOrder(self,root ):
        l= list()
        self.solve(root,l)
        # for revrsal order traveral just revrse the list.
        return l
