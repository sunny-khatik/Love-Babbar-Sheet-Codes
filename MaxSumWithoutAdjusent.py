#https://practice.geeksforgeeks.org/problems/max-sum-without-adjacents2430/1#
# space in O(n)
class Solution:
	def findMaxSum(self,arr, n):
	    dp = [0]*n
		if n == 1:
		    return arr[0]
	    dp[0]=arr[0]
	    dp[1] = max(arr[0] , arr[1])
	    for i in range(2,n):
	        dp[i]=max(dp[i-2]+arr[i] , dp[i-1])
	    return dp[-1]
    
#contsant space
class Solution:
	def findMaxSum(self,arr, n):
		if n == 1:
		    return arr[0]
	    dp0 =arr[0]
	    dp1 = max(arr[0] , arr[1])
	    mx = max(arr[0] , arr[1])
	    for i in range(2,n):
	        mx = max(dp0+arr[i] , dp1)
	        dp0=dp1
	        dp1=mx
	    return mx
