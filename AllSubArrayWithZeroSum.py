# https://practice.geeksforgeeks.org/problems/zero-sum-subarrays1825/1#
from collections import defaultdict
class Solution:
    #Function to count subarrays with sum equal to 0.
    def findSubArrays(self,arr,n):
        #return: count of sub-arrays having their sum equal to 0
        d = defaultdict(lambda : 0)
        prefsum=0
        for i in range(n):
            prefsum+=arr[i]
            d[prefsum]+=1
        ans = 0
        for i in d:
            ans+=(d[i]*(d[i]-1)//2)
            if i == 0:
                ans+=d[i]
        return ans
