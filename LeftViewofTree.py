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
