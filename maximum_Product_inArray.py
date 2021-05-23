# https://practice.geeksforgeeks.org/problems/maximum-product-subarray3604/1#
# see dhruv goyals video for understand the solution
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		# code here
		res = 1
		mini , maxi = 1,1
		for i in arr:
		    if i > 0:
		        maxi = maxi * i
		        mini = min(mini*i , 1)
		    elif i < 0:
		        mini , maxi = maxi , mini
		        mini = mini * i
		        maxi = max(1, maxi*i)
		    else:
		        maxi, mini = 1,1
		    res = max(maxi, res)
        return res
