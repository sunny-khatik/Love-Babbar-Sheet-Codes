# https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/
# https://www.geeksforgeeks.org/longest-palindromic-substring-set-2/
#DP is also there
class Solution:
    def longestPalin(self, s):
        # code here
        pass
        n=len(s)
        start=0
        mxln=1
        low , high=0,0
        for i in range(1,n):
            #initialize it for even palindrome
            low = i-1
            high = i
            while low>= 0 and high < n and s[low] == s[high]: # check loop
                if high-low+1 > mxln:
                    start=low
                    mxln=high-low+1
                low-=1
                high+=1
            #reintialize the low high for odd palindrome string
            low=i-1
            high=i+1
            while low>=0 and high<n and s[high] == s[low]: #chek loop
                if high-low+1 > mxln:
                    start=low
                    mxln=high-low+1
                high+=1
                low-=1
        return s[start:start+mxln]
