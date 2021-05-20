# https://leetcode.com/problems/minimum-window-substring/

import sys
from collections import defaultdict 
class Solution:
    def assign(self):
        return 0
    def minWindow(self, s: str, t: str) -> str:
        d = defaultdict(self.assign)
        for i in t:
            d[i]+=1
        count = len(t)
        start , end= 0, 0
        ans = sys.maxsize
        startInd = 0
        for end in range(len(s)):
            if s[end] in d:
                d[s[end]]-=1
                if d[s[end]] >= 0:
                    count-=1
            if count == 0:
                while True:
                    if s[start] in d:
                        if d[s[start]] < 0:
                            d[s[start]]+=1
                        else:
                            break
                    start+=1
                if ans > end-start+1:
                    ans = end-start+1
                    startInd = start
        if ans == sys.maxsize:
            return ""
        else:
            return s[startInd:ans+startInd]
        
