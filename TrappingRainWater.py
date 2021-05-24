# see striver TUF sheet solution this is O(2n) space complexity solution
# it has better than this which has O(1) space complexity solution just see video for that.
# striver TUF ytube channel has explained a solution of 2 pointer approch.



# https://practice.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1#
class Solution:
    def trappingWater(self, arr,n):
        #Code here
        l1,r1=0,0
        lmax=list() 
        rmax=list()
        for i in range(n):
            l1 = max(l1 , arr[i])
            lmax.append(l1)
        for i in range(n-1,-1,-1):
            r1 = max(r1, arr[i])
            rmax.append(r1)
        res=0
        for i in range(n):
            res+=(min(lmax[i] , rmax[n-1-i])-arr[i])
        return res
