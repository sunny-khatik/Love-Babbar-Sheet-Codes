from collections import defaultdict
#https://practice.geeksforgeeks.org/problems/egg-dropping-puzzle-1587115620/1#
import sys
def ikm():
        return -1
d = defaultdict(ikm)
class Solution:
    
    #Function to find minimum number of attempts needed in 
    #order to find the critical floor.
    def eggDrop(self,n, k):
        # code here
        if n == 1:
            return k
        if k == 1 or k == 0:
            return k
        if d[str(n)+" "+str(k)] != -1:
            return d[str(n)+" "+str(k)]
        d[str(n)+" "+str(k)]  = sys.maxsize
        
        for j in range(1,k+1):
            if d[str((n-1))+" "+str((j-1))] != -1:
                e1 =  d[str((n-1))+" "+str((j-1))]
            else:
                e1 = self.eggDrop(n-1,j-1)
                
            if d[str(n)+" "+str(k-j)] != -1:
                e2 = d[str(n)+" "+str(k-j)]
            else:
                e2 = self.eggDrop(n, k-j)
            
            tmp = 1 + max(e1 , e2) 
            d[str(n)+" "+str(k)]  = min(d[str(n)+" "+str(k)]  , tmp)
        return d[str(n)+" "+str(k)]  
