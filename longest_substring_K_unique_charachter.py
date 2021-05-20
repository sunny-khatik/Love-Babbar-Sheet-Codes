# https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1

#from tuf guy
from collections import defaultdict 
class Solution:
    def assign(self):
        return 0
    
    def longestKSubstr(self, s, k):
        # code 
        d = defaultdict(self.assign)
        if k > len(s) or k > len(set(s)):
            return -1
        start , end , ans , n = 0, 0, -1, len(s)
        while end < n:
            d[s[end]]+=1
            while len(d) > k:
                d[s[start]]-=1
                if d[s[start]] <= 0:
                    del d[s[start]]
                start+=1
            ans = max(ans , end-start+1)
            end+=1
                    
        return ans

#  from aditya varma
from collections import defaultdict 
class Solution:
    def assign(self):
        return 0
    
    def longestKSubstr(self, s, k):
        # code 
        d = defaultdict(self.assign)
        ans = -1
        i ,j=0, 0
        n = len(s)
        while j < n:
            d[s[j]]+=1
            if len(d) < k:
                j+=1
            elif len(d) == k:
                ans = max(ans , j-i+1)
                j+=1
            else:
                while len(d) > k:
                    d[s[i]]-=1
                    if d[s[i]] <= 0:
                        del d[s[i]]
                    i+=1
                j+=1
        return ans
