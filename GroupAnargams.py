#Tech Dose
# https://practice.geeksforgeeks.org/problems/print-anagrams-together/1# 
from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(lambda:[])
        for i in strs:
            tmp = "".join(sorted(i))

            d[tmp].append(i)
        ans=[]
        for i in d:
            ans.append(d[i])
        return ans
