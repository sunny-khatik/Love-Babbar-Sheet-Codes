# https://practice.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1#
# my own solution

import sys
class Solution:

    def findMinDiff(self, a,n,m):
        ans = sys.maxsize
        a.sort()
        # print(a)
        if n == m:
            return a[n-1]-a[0]
        for i in range(n-m+1):
            # print(a[m-1+i],a[i])
            ans = min(ans , a[m-1+i]-a[i])
            # print(ans)
        return ans
