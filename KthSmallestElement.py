# https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1#
# aditya varma
from heapq import heapify, heappop, heappush
class Solution:
    def kthSmallest(self,arr, l, r, k):
        h= list()
        for i in range(k):
            h.append(-1*arr[i])
        heapify(h)
        # print(h)
        for i in range(k,n):
            heappush(h,-1*arr[i])
            heappop(h)
        return heappop(h)*-1
