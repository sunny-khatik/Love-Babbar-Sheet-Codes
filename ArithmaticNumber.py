# https://practice.geeksforgeeks.org/problems/arithmetic-number2815/1#
# code library 
# Do checkout the solutions and article on it
class Solution:
    def solve(self,mid,n):
        c , f=0,5
        while f<=mid:
            c+=mid//f
            f*=5
        return c >= n
    def findNum(self, n : int):
        # Complete this function
        if n == 1:
            return 5
        start = 6
        end= 5*n
        ans=-1
        while start <= end:
            mid =  start+ (end-start)//2
            if self.solve(mid,n):
                ans=mid
                end=mid-1
            else:
                start=mid+1
        return ans
