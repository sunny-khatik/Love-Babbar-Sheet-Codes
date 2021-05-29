# https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
# https://practice.geeksforgeeks.org/problems/parenthesis-checker2744/1#
class Solution:
    def ispar(self,x):
        # code here
        n = len(x)
        if n%2 == 1:
            return False
        else:
            x= list(x)
            stack = list()
            for i in range(n):
                if x[i] == "{" or x[i] == "(" or x[i] == "[":
                    stack.append(x[i])
                else:
                    if len(stack) > 0:
                        char = stack[-1]
                        if (char == "[" and x[i] == "]") or (char == "{" and x[i] == "}") or (char == "(" and x[i] == ")"):
                            stack.pop()
                        else:
                            return False
                    else:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False
