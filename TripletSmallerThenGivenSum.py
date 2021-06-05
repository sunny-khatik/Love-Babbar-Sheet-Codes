# https://practice.geeksforgeeks.org/problems/count-triplets-with-sum-smaller-than-x5549/1#
class Solution:
    def countTriplets(self, arr, n, sums):
        arr.sort()
        ans = 0
        for i in range(n-2):
            start = i+1
            end = n-1
            # print(i,start,end)
            while start < end:
                if arr[start]+arr[end]+arr[i] >= sums:
                    end-=1
                else:
                    ans+=(end-start)
                    start+=1
        return ans
