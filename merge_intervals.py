# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        tmp= intervals[0]
        # print("hell",intervals)
        for i in intervals:
            if tmp[1] >= i[0]:
                tmp[1] = max(tmp[1] , i[1])
                tmp[0] = min(tmp[0] , i[0])
            else:
                ans.append(tmp)
                tmp = i
        ans.append(tmp)
        return ans
 #O(1) space complexity
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ind=0
        for i in range(1,len(intervals)):
            if intervals[ind][1] >= intervals[i][0]:
                intervals[ind][1]=max(intervals[ind][1] ,intervals[i][1])
            else:
                ind+=1
                intervals[ind]=intervals[i]
        return intervals[:ind+1]
        
            
