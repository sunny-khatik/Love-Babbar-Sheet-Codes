from heapq import heapify, heappop, heappush
class Solution:

	def kLargest(self,arr, n, k):
		# code here
		heap=arr[:k]
		heapify(heap)
		for i in range(k,n):
		    heappush(heap,arr[i])
		    heappop(heap)
		l=list()
		while heap:
		    l.append(heappop(heap))
	    return l[::-1] #beacause we have to return elemnrt in non ascending order
