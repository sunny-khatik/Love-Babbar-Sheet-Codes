# tech dose
# aditya varma see video of them.
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left=[0]*n
        right=[0]*n
        stack=list()
        maxi=0
        for i in range(n):
            if len(stack) == 0:
                left[i]=0
                stack.append(i)
            else:
                while len(stack) != 0 and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                left[i]=0 if len(stack) == 0 else stack[-1]+1
                stack.append(i)
        while len(stack) != 0:
            stack.pop()
        for i in range(n-1,-1,-1):
            if len(stack) == 0:
                right[i]=n-1
                stack.append(i)
            else:
                while len(stack) != 0 and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                right[i]=n-1 if len(stack) == 0 else stack[-1]-1
                stack.append(i)
        for i in range(n):
            maxi = max(maxi , heights[i]*(right[i]-left[i]+1))
        return maxi
