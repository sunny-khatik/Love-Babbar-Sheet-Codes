# https://practice.geeksforgeeks.org/problems/find-pair-given-difference1559/1
class Solution:
    def findPair(self, arr, L,N):
        #code here
        arr.sort()
        for i in range(L):
            find = self.bst(arr,L,N+arr[i])
            if find != -1:
                return True
        return False
            
    def bst(self,arr,n,x):
        start , end = 0,n-1
        while start <= end:
            mid = start + (end-start)//2
            if arr[mid] == x:
                return arr[mid]
            elif arr[mid] > x:
                end=mid - 1
            else:
                start = mid + 1
        return -1
