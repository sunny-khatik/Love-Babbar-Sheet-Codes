# https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
from collections import deque
class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        l = deque()
        ans=list()
        for i in range(k):
            while l and arr[i] >= arr[l[-1]]:
                l.pop()
            l.append(i)
        for i in range(k,n):
            ans.append(arr[l[0]])
            while l and l[0] <= i-k:
                l.popleft()
            while l and arr[i] >= arr[l[-1]]:
                l.pop()
            l.append(i)
        ans.append(arr[l[0]])
        return ans
