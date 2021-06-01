# aditya varma 
# https://leetcode.com/problems/longest-palindromic-subsequence/submissions/
# https://www.geeksforgeeks.org/longest-palindrome-subsequence-space/
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n , m = len(s) , len(s)
        res = 0
        s1 , s2= s , s[::-1]
        a,b = 0,0
        t= [[0 for i in range(m+1)]for j in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1] == s2[j-1]:
                    t[i][j]=1+t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j],t[i][j-1])
        return t[n][m]
