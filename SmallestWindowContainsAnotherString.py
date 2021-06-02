# https://practice.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string-1587115621/1
import sys
from collections import defaultdict 
class Solution:
    def assign(self):
        return 0
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        #code here
        d = defaultdict(self.assign)
        for i in p:
            d[i]+=1
        count = len(p)
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
            return -1
        else:
            return s[startInd:ans+startInd]
