# https://leetcode.com/problems/maximum-profit-in-job-scheduling/
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = (zip(startTime,endTime,profit))
        jobs = sorted(jobs , key=lambda x:x[1])
        n =len(profit)
        dp = [0]*(n)
        dp[0]=jobs[0][2]
        for i in range(1,n):
            low , high = 0, i-1
            currProf= jobs[i][2]
            last_job= -1
            while low <= high:
                mid = low + (high-low)//2
                if jobs[mid][1] <= jobs[i][0]:
                    last_job=mid
                    low=mid+1
                else:
                    high=mid-1
            if last_job != -1:
                currProf+=dp[last_job]
            exc_thisJob=dp[i-1]
            dp[i]=max(exc_thisJob, currProf)
        return dp[-1]
