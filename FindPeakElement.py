class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.peak(0, len(nums)-1, nums,len(nums))
    
    
    def peak(self,start , end, arr,n):
        
        mid = start +  (end-start)//2
        if ((mid == 0 or arr[mid-1] < arr[mid]) and (mid == n-1 or arr[mid+1] < arr[mid])):
            return mid
        elif mid > 0 and arr[mid-1] > arr[mid]:
            return self.peak(start , mid-1, arr,n)
        else:
            return self.peak(mid+1 , end, arr,n)
        
