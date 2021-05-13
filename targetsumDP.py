class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        s = (target+sum(nums))//2
        if (target+sum(nums))%2 != 0:
            return 0
        elif target > s:
            return 0
        else:
            t = [[0 for i in range(s+1)] for j in range(n+1)]

            for i in range(n+1):
                t[i][0]=1
            for i in range(1,n+1):
                for j in range(0,s+1):  #zero thi start thse kem ke [0,0,0,0,0,0,0,1] type na test case handle karva mate.
                    if nums[i-1]<= j:
                        t[i][j] = t[i-1][j-nums[i-1]] + t[i-1][j]
                    elif nums[i-1] > j:
                        t[i][j]=t[i-1][j]
            return t[n][s]
        
