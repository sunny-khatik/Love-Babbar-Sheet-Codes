# https://www.geeksforgeeks.org/split-the-binary-string-into-substrings-with-equal-number-of-0s-and-1s/
# split count number of string and aslo prints
c0,c1,c=0,0,0
s="11000110010011"
st=list()
cnt = 0 #substring print
prev0,prev1=0,0
for i in range(len(s)):
    if int(s[i]):
        c1+=1
        cnt+=1
        f=i
    else:
        c0+=1
        f=i
    if c1 == c0:
        if s[i] == "0":
            st.append("1"*(cnt)+"0"*(cnt))
        else:
            st.append("0"*(cnt)+"1"*(cnt))
        cnt=0 #cnt 0 bcz string added and we start for new string count
        c+=1

if c1 == c0:
    print(st)
    print(c)
else:
    print(-1)
    
