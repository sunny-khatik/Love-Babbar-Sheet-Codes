#Tuf video 1 solution which has dict and list data structure more 
class Solution:
    def find_permutation(self, s):
        # Code here 
        n=len(s)
        s=list(s)
        ans=list()
        bool = [False]*n
        ds=list()
        self.solve(s,ds,ans ,bool)
        ans.sort()
        return ans
    
    def solve(self,s,ds,ans,bool):
        if len(ds) == len(s):
            ans.append("".join(ds))
            return 
        for i in range(len(s)):
            if not bool[i]:
                bool[i]=True
                ds.append(s[i])
                self.solve(s,ds,ans,bool)
                ds.pop(len(ds)-1) #pop the last added element and make the index false
                bool[i]=False
        
 #using the next permutation function
class Solution:
    def find_permutation(self, s):
        # Code here 
        s=sorted(s)
        ans=list()
        ans.append("".join(s))
        while self.nextPermutation(s):
            ans.append("".join(s))
        return ans
    
    def nextPermutation(self, nums):
        i= len(nums)-2
        while i > 0 and nums[i] >= nums[i+1]:
            i-=1
        swapVar=0
        for j in range(len(nums)-1 , i , -1):
            if nums[i] < nums[j]:
                swapVar = j
                break
        if i == 0 and swapVar == 0:
            return nums.reverse()
        nums[i] , nums[swapVar] = nums[swapVar] , nums[i]
        r = (len(nums) - (i+1))//2
        for k in range(r):
            nums[k+i+1] , nums[len(nums)-1-k] = nums[len(nums)-1-k],nums[k+i+1]
        return "".join(nums)
