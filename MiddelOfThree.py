# https://practice.geeksforgeeks.org/problems/middle-of-three2926/1#
# see article
class Solution:
    def middle(self,a,b,c):
        x = a - b
        y = b - c 
        z = a - c
        if x*y > 0:
            return b
        elif y*z > 0:
            return a
        else:
            return c
