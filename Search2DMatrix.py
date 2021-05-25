# https://leetcode.com/problems/search-a-2d-matrix/
# see striver TUF series Question for better understanding.
#leet code best approch
#if we apeend elemnts in a list so it will give us a sorted array according to leetcode problem description
class Solution:
    def MatrixBinarySearch(self,low,high,mat,n,t):
        if low <= high:
            mid = low + (high-low)//2
            if mat[mid//n][mid%n] == t:
                return True
            elif mat[mid//n][mid%n] > t:
                return self.MatrixBinarySearch(low,mid-1,mat,n,t)
            else:
                return self.MatrixBinarySearch(mid+1,high,mat,n,t)
        return False
            
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # print(len(matrix), len(matrix[0]))
        return self.MatrixBinarySearch(0,(len(matrix)*len(matrix[0]))-1,matrix,len(matrix[0]),target)
    
   # for sorted row as well as sorted column approch tuf serch matrix video gfg problem best solution 
    class Solution:
	def matSearch(self,mat, N, M, X):
	    i=0
	    j=M-1
	    while i < N and j >= 0:
	        if mat[i][j] == X:
	            return 1
	        elif mat[i][j] < X:
	            i+=1
	        else:
	            j-=1
	    return 0

