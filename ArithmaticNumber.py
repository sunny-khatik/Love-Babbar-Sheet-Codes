# https://practice.geeksforgeeks.org/problems/arithmetic-number2815/1#
# code library 
# Do checkout the solutions and article on it
#number is there on series or not with given a and d.
class Solution:
    def solve(self,mid,n):
        c , f=0,5
        while f<=mid:
            c+=mid//f
            f*=5
        return c >= n
    def findNum(self, n : int):
        # Complete this function
        if n == 1:
            return 5
        start = 6
        end= 5*n
        ans=-1
        while start <= end:
            mid =  start+ (end-start)//2
            if self.solve(mid,n):
                ans=mid
                end=mid-1
            else:
                start=mid+1
        return ans
    
#find missing number in a arithmtic sequance.
def findmissNum(start , end, arr,diff):
    while start <= end:
        mid = start + (end-start)//2
        if mid+1 < n and arr[mid+1] != arr[mid]+diff:
            return arr[mid]+diff
        elif mid > 0 and arr[mid] != arr[mid-1]+diff:
            return arr[mid-1]+diff
        elif arr[mid] == arr[0]+mid*diff:
            start = mid+1
        else:
            end=mid-1
    return -1
    
arr = [2,4,8,10,12,14,16,18,20,22,24]
n = len(arr)
print(findmissNum(0,n-1,arr,(arr[n-1]-arr[0])//n))
