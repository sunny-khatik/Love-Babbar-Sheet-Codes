# code library
# https://practice.geeksforgeeks.org/problems/construct-tree-1/1
class Solution:
    def __init__(self):
        self.ind = 0
    def solve(self,pre,lb,ub,d):
        if lb > ub:
            return 
        new = Node(pre[self.ind])
        self.ind+=1
        if lb == ub:
            return new
        mid = d[new.data]
        new.left = self.solve(pre,lb,mid-1,d)
        new.right = self.solve(pre,mid+1,ub,d)
        return new
    def buildtree(self, ino, pre,n):
        d = {}
        for i in range(n):
            d[ino[i]] = i
        head = self.solve(pre,0,n-1,d)
        return head
