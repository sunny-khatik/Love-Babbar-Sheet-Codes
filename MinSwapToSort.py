# https://practice.geeksforgeeks.org/problems/minimum-swaps/1#
#last solution
class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, arr):
		d= {}
		tmp= arr.copy()
		tmp.sort()
		for i in range(len(nums)):
		    d[nums[i]] = i
		swap=0
		jagya= 0
	    for i in range(len(nums)):
	        if arr[i] != tmp[i]:
	            swap+=1
	            jagya = arr[i]
	            arr[i] , arr[d[tmp[i]]] = arr[d[tmp[i]]] , arr[i]
	            d[jagya]=d[tmp[i]]
	            d[tmp[i]]=i
	    return swap
