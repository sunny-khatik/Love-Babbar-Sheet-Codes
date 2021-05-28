#see AAditya Rajivs video for explination
#value ,index NoOffrow , ListSize : pushed element in heap
import sys
from heapq import heapify , heappush, heappop
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n=len(nums)
        l=list()
        mn= sys.maxsize
        mx= -sys.maxsize-1
        for i in range(n):
            l.append([nums[i][0],0,i,len(nums[i])])
            mn=min(mn , nums[i][0])
            mx=max(mx , nums[i][0])
        heapify(l)
        rang = sys.maxsize
        low , high = sys.maxsize, -sys.maxsize-1
        while l:
            tmp = heappop(l)
            maymin = tmp[0]
            if rang > mx-maymin:
                mn = maymin
                rang = mx-mn
                low=mn
                high=mx
            if tmp[1] == tmp[3]-1:
                break
            tmp[1]+=1
            heappush(l,[ nums[tmp[2]][tmp[1]]  ,tmp[1],tmp[2],tmp[3]])
            mx = max(mx, nums[tmp[2]][tmp[1]])
        return [low,high]
        
        
        
        
            
                
            
        
