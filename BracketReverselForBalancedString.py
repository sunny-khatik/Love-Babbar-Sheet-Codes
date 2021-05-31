# https://practice.geeksforgeeks.org/problems/count-the-reversals0401/1#
# see GFG video tutorial for better under standing.
def countRev (s):
    # your code here
    if len(s)%2 == 1:
        return -1
    stack=list()
    openn , closs=0 ,0
    for i in range(len(s)):
        if len(stack) > 0 and s[i] == "}" and stack[-1] == "{":
            stack.pop()
        else:
            stack.append(s[i])
            # after balancinfg stack count the number of open close bracket.
    for i in stack:
        if i == "{":
            openn+=1
        else:
            closs+=1
    
    return (openn//2 + openn%2 + closs//2 + closs%2)
    
