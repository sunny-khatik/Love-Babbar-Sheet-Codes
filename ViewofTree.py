# Code library
# https://www.geeksforgeeks.org/print-left-view-binary-tree/
def LeftView(root):
    if root == None:
        return []
    l = list()
    q = list()
    q.append(root)
    while len(q) > 0:
        n = len(q)
        for i in range(n):
            tmp = q.pop(0)
            if i == 0:  #change print first node of level
                l.append(tmp.data)
            if tmp.left != None:
                q.append(tmp.left)
            if tmp.right != None:
                q.append(tmp.right)
    return l

#right view level order taversal
#code librry
# https://practice.geeksforgeeks.org/problems/right-view-of-binary-tree/1
class Solution:
    #Function to return list containing elements of right view of binary tree.
    def rightView(self,root):
        if root == None:
            return []
        l = list()
        q = list()
        q.append(root)
        while len(q) > 0:
            n = len(q)
            for i in range(n):
                tmp = q.pop(0)
                if i == n-1:   #change print last node of level
                    l.append(tmp.data)
                if tmp.left != None:
                    q.append(tmp.left)
                if tmp.right != None:
                    q.append(tmp.right)
        return l
# top view of tree
# code library
# same code but stratagy changes.
# https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1#
class Solution:
    def topView(self,root):
        if root == None:
            return []
        q = list()
        d = {}
        q.append([root, 0])
        while len(q) > 0:
            tmp = q.pop(0)
            node = tmp[0]
            height = tmp[1]
            if height not in d:
                d[height] = node.data
            if node.left != None:
                q.append([node.left,height-1])
            if node.right != None:
                q.append([node.right,height+1])
        ans= list()
        #for output left to right
        for i,j in sorted(d.items(),key=lambda x:x[0]):
            ans.append(j)
        return ans
