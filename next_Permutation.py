# https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i= len(nums)-2
        while i > 0 and nums[i] >= nums[i+1]:
            print(nums[i] , nums[i+1])
            i-=1
        swapVar=0
        for j in range(len(nums)-1 , i , -1):
            # print(nums[i] , nums[j])
            if nums[i] < nums[j]:
                swapVar = j
                break
        if i == 0 and swapVar == 0:
            return nums.reverse()
        print(i , swapVar)
        nums[i] , nums[swapVar] = nums[swapVar] , nums[i]
        r = (len(nums) - (i+1))//2
        for k in range(r):
            nums[k+i+1] , nums[len(nums)-1-k] = nums[len(nums)-1-k],nums[k+i+1]
        return nums
                
            
