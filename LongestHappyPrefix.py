#Happy Coding last 10 minute solution
class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        j = 0
        lps = [0]*n
        for i in range(1,n):
            while s[j] != s[i] and j > 0:
                j = lps[j-1]
            if s[i] == s[j]:
                lps[i] = j+1
                j+=1
        return s[:lps[-1]]
      
   # from tushar roy solution
  class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        j = 0
        lps = [0]*n
        i = 1
        while i < n:
            if s[i] == s[j]:
                lps[i]=1+j
                i+=1
                j+=1
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    lps[i]=0
                    i+=1
        return s[:lps[-1]]
            
                
                
        
