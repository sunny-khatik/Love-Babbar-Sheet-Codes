# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimal = sys.maxsize
        profit =0
        for i in range(len(prices)):
            minimal = min(minimal, prices[i])
            profit = max(profit , prices[i]-minimal)
        return profit
