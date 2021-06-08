# https://practice.geeksforgeeks.org/problems/arithmetic-number2815/1#
# code library 
# Do checkout the solutions and article on it
#number is there on series or not with given a and d.
class Solution:
    def inSequence(self, a,b,c):
        # code herei
        
        if c == 0:
            if a  == b:
                return 1
            else:
                return 0
        ans = ((b-a)//c)
        if ans < 0:
            return 0
        else:
            if (b-a)%c == 0:
                return 1
            else:
                return 0
    
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
