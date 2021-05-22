# https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1
# see dhruv goyel video for solution.
# User function Template for python3
from collections import defaultdict
class Solution:
    def a(self):
        return 0
    def getPairsCount(self, arr, n, k):
        # code here
        c = 0
        d = defaultdict(self.a)
        for i in arr:
            d[i]+=1
        for i in arr:
            if 2*i == k: #the case where l = [3,3,3,1] k = 6
                c+=max(0 , d[i]-1)
            else:
                c+=d[k-i]
        return c//2
