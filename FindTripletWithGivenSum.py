# User function Template for python3
# https://practice.geeksforgeeks.org/problems/triplet-sum-in-array-1587115621/1#
# see coding simplified videos
# https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/
class Solution:
     
    #Function to find if there exists a triplet in the 
    #array A[] which sums up to X.
    def find3Numbers(self,a, n, k):
        # Your Code Here
        a.sort()
        bool = False
        for i in range(n-2):
            tsum = k - (a[i])
            l = i+1
            r = n-1
            while l < r:
                t = a[l]+a[r]
                if t == tsum:
                    bool = True
                    l+=1
                    r-=1
                    break
                elif t < tsum:
                    l+=1
                else:
                    r-=1
            if bool:
                break
        if bool:
            return 1
        else:
            return 0
