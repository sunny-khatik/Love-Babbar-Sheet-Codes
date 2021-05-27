# make use of dictionary and heap
# https://www.geeksforgeeks.org/how-to-maintain-dictionary-in-a-heap-in-python/
class Solution:
    def reorganizeString(self, s: str) -> str:
        cntr = collections.Counter(s)
        n=len(s)
        h = [(-v , k) for k,v in cntr.items()]
        heapq.heapify(h)
        maxi = -h[0][0]
        tmp=[""]*n
        if maxi > (n+1)//2:
            return ""
        else:
            i = 0
            while h:
                cnt,char = heapq.heappop(h)
                cnt*=-1
                for j in range(cnt):
                    tmp[i]=char
                    i+=2
                    if i >= n:
                        i=1
            return "".join(tmp)                
        
