# https://practice.geeksforgeeks.org/problems/product-array-puzzle4525/1#
class Solution:
    def productExceptSelf(self, nums, n):
        prod = [0]*n
        #code here
        t1, t2 = 1,1
        for i in range(n):
            prod[i]=t1
            t1*=arr[i]
        # print(*prod)
        for i in range(n-1,-1,-1):
            prod[i]*=t2
            t2*=arr[i]
        # print(*prod)
        return prod
