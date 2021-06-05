# https://practice.geeksforgeeks.org/problems/zero-sum-subarrays1825/1#
#see striver solution
from collections import defaultdict
import sys
def maxLen(n, arr):
    d = defaultdict(lambda : -1)
    prefsum=0
    mx = 0
    for i in range(n):
        prefsum+=arr[i]
        if prefsum == 0:
            mx = max(mx , i+1)
        elif d[prefsum] == -1:
            d[prefsum] = i
        else:
            mx = max(mx , i-d[prefsum])
    return mx
