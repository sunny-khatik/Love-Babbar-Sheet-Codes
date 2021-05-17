from collections import defaultdict
class Solution:
    # @param A : string
    # @return an integer
    def intialize(self):
        return -1
    def cnttrue(self, s):
        n = len(s)
        d = defaultdict(self.intialize)
        return self.exp(s,0,n-1,1, d)
    
    def exp(self, s, i , j , istrue,dp):
    
        if i > j:
            return 0
        
        if i == j:
            if istrue == 1:
                return 1 if s[i] == "T" else 0
            else:
                return 1 if s[i] == "F" else 0
        
        if dp["{} {} {}".format(i,j,istrue)] != -1:
            return dp["{} {} {}".format(i,j,istrue)]
        tmp = 0
        
        for k in range(i+1,j,2):
            if dp["{} {} {}".format(i,k-1,1)]!= -1:
                lt = dp["{} {} {}".format(i,k-1,1)]
            else:
                lt= self.exp(s,i,k-1,1,dp)
                
            if dp["{} {} {}".format(i,k-1,0)] != -1:
                lf = dp["{} {} {}".format(i,k-1,0)]
            else:
                lf= self.exp(s,i,k-1,0,dp)
                
            if dp["{} {} {}".format(k+1,j,1)] != -1:
                rt = dp["{} {} {}".format(k+1,j,1)]
            else:
                rt = self.exp(s,k+1,j,1,dp)
                
            if dp["{} {} {}".format(k+1,j,0)] != -1:
                rf = dp["{} {} {}".format(k+1,j,0)]
            else:
                rf = self.exp(s,k+1,j,0,dp)
            
            if s[k] == "&":
                if istrue == 1:
                    tmp = tmp + (rt*lt)
                else:
                    tmp = tmp + (rf*lf) + (rt*lf) + (rf*lt)
            elif s[k] == "|":
                if istrue == 1:
                    tmp = tmp + (lt*rt) + (lf*rt) + (lt*rf)
                else:
                    tmp = tmp + (lf*rf)
                    
            elif s[k]== "^":
                if istrue == 1:
                    tmp = tmp + (lf*rt) + (rf*lt)
                else:
                    tmp = tmp + (lt*rt) + (lf*rf)
                    
        dp["{} {} {}".format(i,j,istrue)] = tmp%(1003)
            
        return tmp%(1003)
