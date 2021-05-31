# https://practice.geeksforgeeks.org/problems/count-palindromic-subsequences/1#
# code library
def countPs(self,string):
    # Code here
        n = len(string)
        dp = [[-1 for i in range(1001)]for j in range(1001)]
        return self.cnt(string, 0, n-1,dp)%1000000007
    
    def cnt(self, s, i, j, dp):
        if i > j:
            return 0
        if i == j:
            return 1
        if dp[i][j] != -1:
            return dp[i][j]
           
        if dp[i+1][j] != -1:
            left = dp[i+1][j]
        else:
            left = self.cnt(s,i+1,j,dp)
        if dp[i][j-1] != -1:
            right = dp[i][j-1]
        else:
            right = self.cnt(s,i,j-1,dp)
        if s[i] == s[j]:
            dp[i][j] = 1 +left +right 
            return dp[i][j]
        else:
            if dp[i+1][j-1] != -1:
                mid = dp[i+1][j-1]
            else:
                mid = self.cnt(s,i+1,j-1,dp)
            dp[i][j] = left +right- mid
            return dp[i][j]
        
        
class Solution:
    # Your task is to complete this function
    # Function should return an integer
    def countPs(self,string):
        # Code here
        n=len(string)
        cps=[[0 for i in range(n+1)] for j in range(n+1)]
        for i in range(n):
            cps[i][i]=1
        for l in range(2, n+1):
            for i in range(n):
                k=l+i-1
                if k<n:
                    if string[i]==string[k]:
                        cps[i][k] = cps[i][k-1]+cps[i+1][k]+1
                    else:
                        cps[i][k] = cps[i][k-1] + cps[i+1][k] - cps[i+1][k-1]
        return cps[0][n-1]%1000000007
