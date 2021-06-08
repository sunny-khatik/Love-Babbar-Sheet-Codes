# https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1
import sys
class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):'
        #striver tuf solution
        # if n > m:
        #     return self.kthElement(arr2,arr1,m,n,k)
        # low = max(0,k-m)
        # high = min(k,n)
        # while low <= high:
        #     c1= low+ (high-low)//2
        #     c2=k-c1
        #     l1 = arr1[c1-1] if c1 != 0 else -sys.maxsize+1
        #     l2 = arr2[c2-1] if c2 != 0 else -sys.maxsize+1
        #     r1 = arr1[c1] if c1 != n else sys.maxsize
        #     r2 = arr2[c2] if c2 != m else sys.maxsize
        #     if l1 <= r2 and l2 <= r1:
        #         return max(l1,l2)
        #     elif l1 > r2:
        #         high = c1-1
        #     else:
        #         start = c1+1
        # return 1
        i,j,kk=0,0,0
        while i < n and j < m:
            if arr1[i] < arr2[j]:
                kk+=1
                if kk == k:
                    return arr1[i]
                i+=1
            else:
                kk+=1
                if kk == k:
                    return arr2[j]
                j+=1
        while i < n:
            kk+=1
            if kk == k:
                return arr1[i]
            i+=1
        while j < m:   
            kk+=1
            if kk == k:
                return arr2[j]
            j+=1
            
