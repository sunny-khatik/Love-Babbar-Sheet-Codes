d = 256 #Number of Characters
class Solution:
    def search(self, pat, txt):
        M = len(pat)
        N = len(txt)
        i = 0
        j = 0
        p = 0    # hash value for pattern
        t = 0    # hash value for txt
        h = 1    # For removel of last  window and make hash to roll
        q = 101
        l = list()
        
        
        #h for slid window and get the next valuw
        for i in range(M-1):
            h = (h*d)%q
        
        for i in range(M):
            p = (d*p + ord(pat[i]))%q
            t = (d*t + ord(txt[i]))%q
     
        for i in range(N-M+1):
            if p==t:
                for j in range(M):
                    if txt[i+j] != pat[j]:
                        break
                    else: j+=1
                if j==M:
                    l.append(i+1)
            if i < N-M:  #here i+m < n because we taking txt[i+m]
                t = (d*(t-ord(txt[i])*h) + ord(txt[i+M]))%q
                if t < 0: # t < 0 then add prime value in it simply
                    t = t+q
        if l:
            return l
        else:
            return [-1]
