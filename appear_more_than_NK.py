# https://www.geeksforgeeks.org/given-an-array-of-of-size-n-finds-all-the-elements-that-appear-more-than-nk-times/

from collections import defaultdict
class Solution:
    def assign(self):
        return 0
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr,n,k):
        #Your code here
        c=0
        d = defaultdict(self.assign)
        for i in arr:
            d[i]+=1
        count = n//k
        for i in d:
            # print(d[i] , count)
            if d[i] > count:
                c+=1
        return c
