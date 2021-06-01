# https://practice.geeksforgeeks.org/problems/smallest-distant-window3132/1#
# https://www.geeksforgeeks.org/smallest-window-contains-characters-string/
# https://www.geeksforgeeks.org/length-smallest-sub-string-consisting-maximum-distinct-characters/
#GFG article solution
import sys
from collections import defaultdict
class Solution:
    def findSubString(self, s):
        n= len(s)
        d = defaultdict(lambda : 0)
        count,unique = 0, len(set(s))
        minwsize = sys.maxsize
        start=0
        for j in range(n):
            d[s[j]]+=1
            if d[s[j]] == 1:
                count+=1
            if count == unique:
                while d[s[start]] > 1:
                    if d[s[start]] > 1:
                        d[s[start]]-=1
                    start+=1
                minwsize = min(minwsize, j-start+1)
        return minwsize
