# code library
# https://practice.geeksforgeeks.org/problems/construct-tree-1/1
#in and pre
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

    # https://practice.geeksforgeeks.org/problems/tree-from-postorder-and-inorder/1
    #in and post
    class Test:
    def __init__(self,n):  #n start from last because of post order.
        self.ind = n
    def solve(self,post,d,lb,ub):
        if lb > ub:
            return None
        if self.ind < 0:
            return 
        new = Node(post[self.ind])
        self.ind-=1
        if lb == ub:
            return new
        mid = d[new.data]
        new.right = self.solve(post,d,mid+1,ub) #it comes right first and then left
        new.left = self.solve(post,d,lb,mid-1)
        return new
#Function to return a tree created from postorder and inoreder traversals.
def buildTree(ino, post, n):
    # your code here
    d ={}
    for i in range(n):
        d[ino[i]]  = i
    o = Test(n-1)
    head = o.solve(post,d,0,n-1)
    return head
