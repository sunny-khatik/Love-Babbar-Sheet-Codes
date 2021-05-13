
# https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1
# itertive function
def knapSack(self,c, wt, val, n):
        t = [[-1 for i in range(c+1)] for j in range(n+1)]
        for i in range(n+1):
            for j in range(c+1):
                if i == 0 or j == 0:
                    t[i][j] = 0
        for i in range(1,n+1):
            for j in range(1,c+1):
                if(wt[i-1] <= j):
                    t[i][j]=max(val[i-1]+t[i-1][j-wt[i-1]] , t[i-1][j])
                elif wt[i-1] > j:
                    t[i][j]=t[i-1][j]
        return t[n][c]
      
# Recursive function
class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
        #recursive ma error ayi jase beta
    def knapSack(self,c, wt, val, n):
        if c == 0 or n == 0:
            return 0
        if wt[n-1] <= c:
            return max (val[n-1]+self.knapSack(c-wt[n-1],wt,val,n-1) , self.knapSack(c,wt,val,n-1))
        elif wt[n-1] > c:
            return self.knapSack(c,wt,val,n-1)
