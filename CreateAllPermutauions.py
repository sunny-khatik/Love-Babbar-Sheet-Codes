#Tuf video 1 solution which has dict and list data structure more 
class Solution:
    def find_permutation(self, s):
        # Code here 
        n=len(s)
        s=list(s)
        ans=list()
        bool = [False]*n
        ds=list()
        self.solve(s,ds,ans ,bool)
        ans.sort()
        return ans
    
    def solve(self,s,ds,ans,bool):
        if len(ds) == len(s):
            ans.append("".join(ds))
            return 
        for i in range(len(s)):
            if not bool[i]:
                bool[i]=True
                ds.append(s[i])
                self.solve(s,ds,ans,bool)
                ds.pop(len(ds)-1) #pop the last added element and make the index false
                bool[i]=False
