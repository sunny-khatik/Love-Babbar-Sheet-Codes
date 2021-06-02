# https://practice.geeksforgeeks.org/problems/isomorphic-strings-1587115620/1#
from collections import defaultdict
class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        l = [0]*26
        t = [0]*26
        if len(str1) != len(str2):
            return False
        for i in range(len(str1)):
            if l[ord(str1[i])-ord("a")] == 0 and t[ord(str2[i])-ord("a")] == 0:
                l[ord(str1[i])-ord("a")] = 1
                t[ord(str2[i])-ord("a")] = 1
            elif l[ord(str1[i])-ord("a")]  != t[ord(str2[i])-ord("a")] :
                return False
        return True
