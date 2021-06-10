#https://practice.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1
class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
        l=list()
        self.printdata(matrix,0,0,r,c,l)
        return l
 
    def printdata(self,arr, i, j, m, n,l):
        if (i >= m or j >= n):
            return
     
        # Print First Row
        for p in range(i, n):
            l.append(arr[i][p])
     
        # Print Last Column
        for p in range(i + 1, m):
            l.append(arr[p][n - 1])
     
        # Print Last Row, if Last and
        # First Row are not same
        if ((m - 1) != i):
            for p in range(n - 2, j - 1, -1):
                l.append(arr[m - 1][p])
     
        # Print First Column, if Last and
        # First Column are not same
        if ((n - 1) != j):
            for p in range(m - 2, i, -1):
                l.append(arr[p][j])
     
        self.printdata(arr, i + 1, j + 1, m - 1, n - 1,l)
