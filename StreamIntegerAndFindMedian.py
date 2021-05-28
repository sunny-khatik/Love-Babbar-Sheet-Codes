#see tech dose video of find median in a stream
#leetcode selection

class MedianFinder:
    def __init__(self):
        self.lowerhalf=list() #max heap
        self.upperhalf=list() #min heap
        

    def addNum(self, num: int) -> None:
        if len(self.lowerhalf) == 0:
            heapq.heappush(self.lowerhalf, -num)
            return
        
        if num <= -self.lowerhalf[0]:
            heapq.heappush(self.lowerhalf, -num) # Go to the max Heap 
        else:
            heapq.heappush(self.upperhalf, num) # Go to the min Heap
            
        
        # If the lowerhalf heap has more elements
        if len(self.lowerhalf) - len(self.upperhalf) == 2:
            heapq.heappush(self.upperhalf, - heapq.heappop(self.lowerhalf))
        
        # If the upperhalf heap has more elements
        elif len(self.upperhalf) - len(self.lowerhalf) == 2:
            heapq.heappush(self.lowerhalf, - heapq.heappop(self.upperhalf)) 
            
        
    def findMedian(self) -> float:
        if len(self.lowerhalf) == len(self.upperhalf):
            return (-1*(self.lowerhalf[0])+(self.upperhalf[0]))/2
        elif len(self.lowerhalf) > len(self.upperhalf):
            return -float(self.lowerhalf[0])
        else:
            return float(self.upperhalf[0])
#GFG seclection

mnheap=list()
mxheap=list()
heapq.heapify(mxheap)
heapq.heapify(mnheap)
class Solution:
        
    def getMedian(self):
        if len(mnheap) == len(mxheap):
            return (-1*(mxheap[0])+(mnheap[0]))/2
        else:
            return -1*mxheap[0]
        
        
    def insertHeaps(self,num):
        if len(mnheap) == len(mxheap):
            if len(mxheap) == 0:
                heapq.heappush(mxheap , -1*num)
            else:
                mxtop=mnheap[0]
                if mxtop < num:
                    heapq.heappop(mnheap)
                    heapq.heappush(mxheap,-1*mxtop)
                    heapq.heappush(mnheap , num)
                else:
                    heapq.heappush(mxheap,-1*num)
        else:
            mxtop=-1*mxheap[0]
            if mxtop < num:
                heapq.heappush(mnheap,num)
            else:
                heapq.heappop(mxheap)
                heapq.heappush(mnheap,mxtop)
                heapq.heappush(mxheap,-1*num) 
