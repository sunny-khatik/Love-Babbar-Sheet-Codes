#User function Template for python3
import sys
dp = [[-1 for i in range(101)] for j in range(101)]
class Solution:
    def matrixChainMemoised(self,p, i, j):
    	if(i == j):
    		return 0
    	
    	if(dp[i][j] != -1):
    		return dp[i][j]
    	
    	dp[i][j] = sys.maxsize
    	
    	for k in range(i,j):
    		dp[i][j] = min(dp[i][j], self.matrixChainMemoised(p, i, k) + self.matrixChainMemoised(p, k + 1, j)+ p[i - 1] * p[k] * p[j])
    	
    	return dp[i][j]

    def matrixMultiplication(self,n,p):
    	i = 1
    	j = n - 1
    	return self.matrixChainMemoised(p, i, j)
            
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends
