# https://practice.geeksforgeeks.org/problems/minimum-swaps-for-bracket-balancing2704/1#
# https://www.geeksforgeeks.org/minimum-swaps-bracket-balancing/
class Solution:
    def minimumNumberOfSwaps(self,S):
        countLeft = 0
        countRight = 0
        chars=S
        swap = 0
        imbalance = 0;
        for i in range(len(chars)):
            if chars[i] == '[':
                countLeft += 1
                if imbalance > 0:
                    swap += imbalance
                    imbalance -= 1
            elif chars[i] == ']':
                countRight += 1
                imbalance = (countRight - countLeft)
        return swap
  
