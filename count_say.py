# see code library solution
# https://leetcode.com/problems/count-and-say/
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        elif n == 2:
            return "11"
        else:
            s = "11"
            for i in range(n-2):
                s+="&"
                t=""
                c=1
                for i in range(len(s)-1):
                    if s[i] != s[i+1]:
                        t += (str(c)+s[i])
                        c=1
                    else:
                        c+=1
            return t
            
                    

        
