# https://practice.geeksforgeeks.org/problems/isomorphic-strings-1587115620/1#
from collections import defaultdict
class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,s1,s2):
        d = defaultdict(lambda:-1)
        n ,m = len(s1),len(s2)
        if n != m:
            return False
        mark = [False]*26
        for i in range(n):
            if d[s1[i]] == -1:
                if mark[ord(s2[i])-ord("a")] == True:
                    return False
                mark[ord(s2[i])-ord("a")] = True
                d[s1[i]] = s2[i]
            elif d[s1[i]] != s2[i]:
                return False
        return True
