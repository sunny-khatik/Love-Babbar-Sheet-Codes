
# https://practice.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1#
# lec - 47 | Apni Kaksha | Zero Sum Subarray
class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        s = set()
        sum=0
        bool = False
        for i in arr:
            s.add(sum)
            sum+=i
            if sum in s:
                bool = True
        return bool
