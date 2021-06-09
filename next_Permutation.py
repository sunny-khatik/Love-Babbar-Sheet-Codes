# https://leetcode.com/problems/next-permutation/
#TUF solution
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i= len(nums)-2
        while i > 0 and nums[i] >= nums[i+1]:
            i-=1
        swapVar=0
        for j in range(len(nums)-1 , i , -1):
            if nums[i] < nums[j]:
                swapVar = j
                break
        if swapVar == 0:
            return nums.reverse()
        nums[i] , nums[swapVar] = nums[swapVar] , nums[i]
        start = i+1
        end = len(nums)-1
        while start < end:
            nums[start], nums[end]=nums[end],nums[start]
            start+=1
            end-=1
        return nums
                
            
