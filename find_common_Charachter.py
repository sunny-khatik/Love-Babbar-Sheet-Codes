# https://leetcode.com/problems/find-common-characters/
import sys
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        t = list()
        for i in range(len(words)):
            t.append([0]*26)
        for i in range(len(words)):
            for j in words[i]:
                t[i][ord(j)-ord("a")]+=1
        ans = list()
        for j in range(26):
            min = sys.maxsize
            for i in range(len(words)):
                if t[i][j] < min:
                    min = t[i][j]
            for k in range(min):
                ans.append(chr(97+j))
        return ans
