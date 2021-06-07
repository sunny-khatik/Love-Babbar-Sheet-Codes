# Aditya varma classsic solution
# https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1
class Solution:
    def valid(self , arr, n, student, mid):
        tmp_st = 1
        sum =  0
        for i in range(n):
            sum+=arr[i]
            if sum > mid:
                tmp_st+=1
                sum = arr[i]
            if tmp_st > student:
                return False
        return True
    #Function to find minimum number of pages.
    def findPages(self,arr, n, m):
        #code here
        if n < m:
            return -1
        start = max(arr)
        end = sum(arr)
        ans= -1
        while start <= end:
            mid = start + (end-start)//2
            if self.valid(arr , n , m, mid):
                ans = mid
                end = mid -1
            else:
                start = mid +1
        return ans
                
