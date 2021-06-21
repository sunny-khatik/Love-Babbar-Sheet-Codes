#stickler thief
# https://leetcode.com/problems/house-robber/
class Solution:
    def solve(self,a,dp,i):
        if i >= len(a):
            return 0
        if dp[i] != -1:
            return dp[i]
        m1  = a[i] +self.solve(a,dp,i+2)
        m2 = self.solve(a,dp,i+1)
        dp[i] = max(m1,m2)
        return dp[i]
    def rob(self, nums: List[int]) -> int:
        dp = [-1]*(len(nums))
        return self.solve(nums,dp,0)  
