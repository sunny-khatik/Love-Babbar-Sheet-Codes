# https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1#
# O(m+n) time complexity approch start from last and find 1 because array is sorted 
# while j>0 assign row for more info chek atricle's last solution
# https://www.geeksforgeeks.org/find-the-row-with-maximum-number-1s/
class Solution:

	def rowWithMax1s(self,arr, n, m):
		# code here
		j=m-1
		rowi=-1
		for i in range(n):
		    while j>=0 and arr[i][j]==1:
		        j-=1
		        rowi=i
	    return rowi
