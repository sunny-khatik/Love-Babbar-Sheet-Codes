# https://www.geeksforgeeks.org/longest-repeating-subsequence/
# https://practice.geeksforgeeks.org/problems/longest-repeating-subsequence2004/1#
class Solution:
	def LongestRepeatingSubsequence(self, str):
	    n=len(str)
	    t = [[0 for i in range(n+1)]for j in range(n+1)]
	    for i in range(1,n+1):
	        for j in range(1,n+1):
	            if str[i-1] == str[j-1] and i != j:
	                t[i][j]=t[i-1][j-1]+1
	            else:
	                t[i][j]=max(t[i-1][j], t[i][j-1])
	    return t[n][n]
