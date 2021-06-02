# https://practice.geeksforgeeks.org/problems/consecutive-elements2306/1#
class Solution:
    def removeConsecutiveCharacter(self, s):
        n=len(s)
        ans=""
        for i in range(n-1):
            if s[i] != s[i+1]:
                ans+=s[i]
        return ans+s[n-1]
