# https://practice.geeksforgeeks.org/problems/min-number-of-flips3210/1
class Solution:
    def minFlips(self, s):
        # Code here
        return min(self.solve(s , "0") , self.solve(s,"1"))
        
    def solve(self, s ,exp):
        count = 0
        for i in range(len(s)):
            if exp != s[i]:
                count+=1
            exp = "1" if exp == "0" else "0"
        return count
