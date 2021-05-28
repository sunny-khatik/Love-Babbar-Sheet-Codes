# see problem it easy use min heap 
# own solution
from heapq import heapify,heappop,heappush
class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,arr,n) :
        ans = 0
        if n == 1:
            return ans
        else:
            heapify(arr)
            while arr:
                if len(arr) >= 2:
                    a,b= heappop(arr), heappop(arr)
                    ans+=(a+b)
                    heappush(arr , a+b)
                else:
                    break
            return ans
