# https://practice.geeksforgeeks.org/problems/word-break1352/1#
# Kartik arora's word break easy explanation
from collections import defaultdict
def assign():
    return -1
def wordBreak(line, dictionary):
    # Complete this function
    n=len(line)
    d = defaultdict(assign)
    for i in dictionary:
        d[i]=1
    dp = [0]*(n+1)
    dp[n]=1
    for i in range(n-1,-1,-1):
        tmp=""
        for j in range(i,n):
            tmp+=line[j]
            if d[tmp] == 1 and dp[j+1]: #word exist iin dict and backword words are 1
                dp[i]=1
    return dp[0]
