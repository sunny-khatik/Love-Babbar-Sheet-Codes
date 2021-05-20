# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
# https://youtu.be/qtVh-XEpsJo (see this for solution last approch)
from collections import defaultdict 
def assign():
    return -1
    
d = defaultdict(assign)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right,ans,n = 0,0,0,len(s)
        while right < n:
            if d[s[right]] != -1:
                left = max(left , d[s[right]]+1)
            d[s[right]] = right
            ans = max(ans , right-left+1)
            right+=1
        return ans
