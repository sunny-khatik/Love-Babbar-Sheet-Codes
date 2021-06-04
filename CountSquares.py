# https://practice.geeksforgeeks.org/problems/count-squares3649/1#
import math
class Solution:
    def countSquares(self, N):
        start = 1
        end = N
        ans = 0
        while start <= end:
            mid = start + (end-start)//2
            if mid*mid == N:
                ans = mid
                break
            elif mid*mid < N:
                start = mid + 1
                ans = mid
            else:
                end = mid -1
        if math.ceil(N**0.5) == N**0.5:
            return ans-1
        else:
            return ans
