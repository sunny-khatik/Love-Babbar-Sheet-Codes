# https://practice.geeksforgeeks.org/problems/smallest-subarray-with-sum-greater-than-x5651/1#
# see Dhruv Goyel's video for this.
# https://www.geeksforgeeks.org/minimum-length-subarray-sum-greater-given-value/
class Solution:
    def sb(self, a, n, x):
        ans=n+1
        l ,r= 0,0
        sum=0
        while r < n:
            while x >= sum and r < n:
                sum+=a[r]
                r+=1
            while sum > x and l < n:
                ans = min(ans , r-l)
                sum-=a[l]
                l+=1
        return ans
