# https://practice.geeksforgeeks.org/problems/count-palindromic-subsequences/1#
# code library
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
