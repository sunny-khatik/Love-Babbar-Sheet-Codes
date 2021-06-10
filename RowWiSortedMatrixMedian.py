#TUF Striver
class Solution:
    def countNum(self, l, target):
        start = 0
        end = len(l)-1
        ans=-1
        while start <= end:
            mid = start + (end-start)//2
            if l[mid] <= target:
                ans= mid
                start = mid+1
            else:
                end = mid-1
        return ans+1
    def median(self, matrix, r, c):
    	#code here 
    	
    	mn, mx = 2001 , 0
    	for i in range(r):
    	    mn = min(mn, matrix[i][0])
    	    mx = max(mx, matrix[i][c-1])
        mn , mx
        while mn <= mx:
            mid = mn + (mx-mn)//2
            total = 0
            for i in range(r):
                total+=self.countNum(matrix[i], mid)
            if total <= (r*c)//2:
                mn = mid+1
            else:
                mx = mid-1
        return mn
