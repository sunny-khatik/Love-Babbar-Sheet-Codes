# see algods video for better solution 
# https://practice.geeksforgeeks.org/problems/kth-element-in-matrix/1#
def count(mat,mid):
    n = len(mat)
    i = len(mat)-1
    j = 0
    c = 0
    while i>= 0 and j<n:
        if mat[i][j] > mid:
            i-=1
        elif mat[i][j] <= mid:
            c+= (i+1)
            j+=1
    return c
            
def solve(mat,low,high,k):
    ans=0
    while low <= high:
        mid = low + (high-low)//2
        counts=count(mat,mid)
        if counts >= k:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
    
def kthSmallest(mat, n, k): #start
    # Your code goes here
    low = mat[0][0]
    high=mat[n-1][n-1]
    return solve(mat,low,high,k)
