#  see dhruv goyels video for bettter approch inplce used two pointer
# lta = take care of less than a
# gtb = take care of greater than b
# https://practice.geeksforgeeks.org/problems/three-way-partitioning/1#
# https://www.geeksforgeeks.org/three-way-partitioning-of-an-array-around-a-given-range/
class Solution:
	def threeWayPartition(self, arr, a, b):
	    # code here
	    n=len(arr)
	    lta=0
	    gtb=n-1
	    curr=0
	    while curr <= gtb:
	        if arr[curr] < a:
	            arr[curr],arr[lta]=arr[lta],arr[curr]
	            curr+=1
	            lta+=1
	        elif arr[curr]> b:
	            arr[curr],arr[gtb]=arr[gtb], arr[curr]
	            gtb-=1
	        else:
	            curr+=1
