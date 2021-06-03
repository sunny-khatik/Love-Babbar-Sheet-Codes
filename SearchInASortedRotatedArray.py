# https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/     problen
# source for code 
# https://www.techiedelight.com/find-number-rotations-circularly-sorted-array/
# see aditya varma search in sorted array you get it
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mnind = 0
        n = len(nums)
        start, end = 0 ,n-1
        if nums[start] <= nums[end]:
            return self.bst(start,end,target,nums)
          
        while start <= end:
            if nums[start] <= nums[end]:
                mnind = start
                break
            mid = start + (end-start)//2
            prev = (mid-1+n)%n
            nextt = (mid+1)%n
            if nums[mid] <= nums[prev] and nums[mid] <= nums[nextt]:
                mnind = mid
                break
            elif nums[start] <= nums[mid]:
                start = mid+1
            elif nums[mid] <= nums[end]:
                end = mid-1
                
        a1 = self.bst(0,mnind-1,target,nums)
        a2 = self.bst(mnind,n-1,target,nums)
        if a1 >= 0:
            return a1
        elif a2 >= 0:
            return a2
        else:
            return -1
          
    def bst(self,start,end,x,nums):
        res = -1
        while start <= end:
            mid = start+(end-start)//2
            if nums[mid] == x:
                res = mid
                break
            elif nums[mid] > x:
                end = mid -1
            else:
                start = mid + 1
        return res
