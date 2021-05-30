# https://leetcode.com/problems/longest-happy-prefix/
# own solution
# tech dose solution for trie
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        mini = 201
        n = len(strs)
        exstr = strs[0]
        for i in range(n):
            mini = min(mini , len(strs[i]))
        c=0
        ans=""
        for i in range(mini):
            for j in range(n):
                if strs[j][i] == exstr[i]:
                    c+=1
            if c == n:
                ans+=exstr[i]
            else:
                break
            c = 0
        return ans
            
            
        
