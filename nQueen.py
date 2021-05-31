#best algo site for this'
# http://techieme.in/solving-the-n-queen-problem/



#  return Number of solution
class Solution:
    def totalNQueens(self, n: int) -> int:
        x = [0]*(n)
        l = list()
        self.nQueen(0,n,x,l)
        return len(l)
        
    def nQueen(self,pos,n,x,l):
        if pos == n:
            l.append(x)
            return
        for i in range(0,n):
            x[pos] = i+1
            if self.place(x,pos):
                self.nQueen(pos+1,n,x,l)
            else:
                x[pos]=-1
                
    def place(self,x ,pos):
        for i in range(0,pos):
            if x[i] == x[pos] or abs(x[i]-x[pos]) == abs(i-pos):
                return False
        return True
      
 #print number of solution anarrengement also in 1D array
l=list()
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        x = [0]*(n)
        self.nQueen(0,n,x)
        print(len(l))
        
    def nQueen(self,pos,n,x):
        if pos == n:
            print(x)
            l.append(x)
            return
        for i in range(0,n):
            x[pos] = i+1
            if self.place(x,pos):
                self.nQueen(pos+1,n,x)
            else:
                x[pos]=-1
                
    def place(self,x ,pos):
        for i in range(0,pos):
            if x[i] == x[pos] or abs(x[i]-x[pos]) == abs(i-pos):
                return False
          
        return True
      
# https://leetcode.com/problems/n-queens/
#leet code hard solution
class Solution:
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        x = [0]*(n)
        ans=list()
        self.nQueen(0,n,x,ans)
        return ans
        
        
        
    def nQueen(self,pos,n,x,ans):
        if pos >= n:
            return self.dot(x,n,ans)
        for i in range(0,n):
            x[pos] = i+1
            if self.place(x,pos,ans):
                self.nQueen(pos+1,n,x,ans)
            else:
                x[pos]=-1
                
    def place(self,x ,pos,ans):
        for i in range(0,pos):
            if x[i] == x[pos] or abs(x[i]-x[pos]) == abs(i-pos):
                return False
        return True

    def dot(self,x,n,ans):
        tmp=[]
        for i in range(n):
            tmp.append(self.dodot(x[i],n,ans))
        ans.append(tmp)
        
        
        
    def dodot(self,i,n,ans):
        res=""
        for j in range(1,n+1):
            if j == i:
                res+="Q"
            else:
                res+="."
        return res
            
        
        
