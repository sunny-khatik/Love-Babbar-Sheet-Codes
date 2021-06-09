#when height is only greater or equals to zero heights are allowed.
import sys
class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr.sort()
        ans=arr[n-1]-arr[0]
        smallest_height=arr[0]+k
        largest_height=arr[n-1]-k
        mn, mx = sys.maxsize , -sys.maxsize+1
        for i in range(n-1):
            mn = min(smallest_height , arr[i+1]-k)
            
            mx=max(largest_height , arr[i]+k)
            if mn < 0:
                continue
            ans = min(ans , mx-mn)
        return ans
#when height less then zero is allowd.
import sys
class Solution:
    def getMinDiff(self, arr, n, k):
        # code 
        # code here
        arr.sort()
        ans=arr[n-1]-arr[0]
        smallest_height=arr[0]+k
        largest_height=arr[n-1]-k
        mn, mx = sys.maxsize , -sys.maxsize+1
        for i in range(n-1):
            mn = min(smallest_height , arr[i+1]-k)
            
            mx=max(largest_height , arr[i]+k)
            ans = min(ans , mx-mn)
        return ans
