
# https://www.interviewbit.com/problems/scramble-string/
from collections import defaultdict
class Solution:
    def intialize(self):
        return -1
    def isScramble(self, s1: str, s2: str) -> bool:  #start
        if sorted(s1) != sorted(s2):
            return 0
        if len(s1) != len(s2):
            return 0
        if s1 == s2:
            return 1
        t = defaultdict(self.intialize)
        return self.solve(s1,s2,t)
    def solve(self, s1, s2,t):
        n=len(s1)
        if s1 == s2:
            return 1
        if n<= 1:
            return 0
        
        key = s1+" "+s2
        if t[key] != -1:
            return t[key]
        flag = 0
        for i in range(1, len(s1)):
            
            if t[s1[0:i]+" "+s2[0:i]] != -1:
                c1_1 = t[s1[0:i]+" "+s2[0:i]]
            else:
                c1_1 = self.solve(s1[0:i] , s2[0:i] , t)
            
            if t[s1[i:]+" "+s2[i:]] != -1:
                c1_2 = t[s1[i:]+" "+s2[i:]]
            else:
                c1_2 = self.solve(s1[i:] , s2[i:] ,t)
            
            c1 = c1_1 and c1_2
            
            if t[s1[:i]+" "+s2[n-i:]] != -1:
                c2_1 = t[s1[:i]+" "+s2[n-i:]]
            else:
                c2_1 = self.solve(s1[:i] , s2[n-i:] ,t)
            if t[s1[i:]+" "+s2[:n-i]] != -1:
                c2_2 = t[s1[i:]+" "+s2[:n-i]]
            else:
                c2_2 = self.solve(s1[i:] , s2[:n-i] ,t)
            c2 = c2_1 and c2_2
            
            if c1 or c2:
                flag = 1
                break
        t[s1+" "+s2] = flag
        return flag
        
