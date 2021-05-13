class Solution:
    def equalPartition(self, n, arr):
        # code here
        sum1 = 0
        sum1 = sum(arr)
        if sum1%2 != 0:
            return 0
        else:
            return self.isSubset(arr,len(arr),sum1//2)
    #using iterative solution     
    def isSubsetIterative(self, arr,n,s):
        t = [[False for i in range(s+1)] for j in range(n+1)]
        for i in range(n+1):
            for j in range(s+1):
                if j == 0:
                    t[i][0] = True
                elif arr[i-1] <= j:
                    t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
                elif arr[i-1] > j:
                    t[i][j]=t[i-1][j]
        if t[n][s] == 1:
            return 1
        else: 
            return 0
    #using recursive approch
    def isSubset(self,arr,n, s):
        if s == 0:
            return 1
        if n == 0 and sum != 0:
            return 0
        if arr[n-1] <= s:
            if self.isSubset(arr,n-1,s-arr[n-1]) or self.isSubset(arr,n-1,s):
                return 1
            else:
                return 0
        else:
            if self.isSubset(arr,n-1,s):
                return 1
            else:
                return 0
  
              
