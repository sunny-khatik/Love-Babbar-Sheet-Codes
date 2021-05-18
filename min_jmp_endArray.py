#User function Template for python3  
#https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1#
# https://www.geeksforgeeks.org/minimum-number-jumps-reach-endset-2on-solution/
class Solution:
	def maxJumps(self, arr, n):
	    maxr = arr[0]
	    step = arr[0]
	    jmp = 1
	    for i in range(1,n):
	        if i == n-1:
	            return jmp
	        maxr = max(maxr , i+arr[i])
	        step-=1
	        if step == 0:
	            jmp+=1
	            if i >= maxr:
	                return -1
	            step = maxr-i
	     return jmp 
