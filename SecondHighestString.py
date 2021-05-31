# https://practice.geeksforgeeks.org/problems/second-most-repeated-string-in-a-sequence0534/1#
from collections import Counter
class Solution:
    def assign(self):
        return 0
    def secFrequent(self, arr, n):
        # code here
        d = Counter(arr)
        max1=d[0]
        string = ""
        for i in d:
            if d[i] > max1:
                max1=d[i]
                string = i
        for i in d:
            if d[i] == max1:
                d[i]=0
        finlans=""
        max2=-10000
        for i in d:
            if d[i] > max2:
                max2=d[i]
                finlans = i
        return finlans
