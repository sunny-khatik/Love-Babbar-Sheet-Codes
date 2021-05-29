#code library
def subseq(t,i,n,s):
    if i == n:
        print(t)
    else:
        subseq(t,i+1,n,s)
        t+=s[i]
        subseq(t,i+1,n,s)
    
    
s="abc"
n=len(s)
subseq("",0,len(s),s)
