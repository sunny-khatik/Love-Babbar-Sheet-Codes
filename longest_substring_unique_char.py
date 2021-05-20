# https://www.interviewbit.com/problems/longest-substring-without-repeat/
# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
# https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1#
# https://youtu.be/qtVh-XEpsJo (see this for solution last approch)
from collections import defaultdict 
class Solution:
    # @param A : string
    # @return an integer
    def assign(self):
        return -1
    def lengthOfLongestSubstring(self, A):
        left,right,ans,n = 0,0,0,len(A)
        d = defaultdict(self.assign)
        while right < n:
            if d[A[right]] != -1:
                left = max(left , d[A[right]]+1)
            d[A[right]] = right
            ans = max(ans , right-left+1)
            right+=1
        return ans


