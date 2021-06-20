def biggerIsGreater(w):
    n = len(w)
    i = n-2
    while i >= 0 and w[i] >= w[i+1]:
        i-=1
    swapvar = 0
    for j in range(n-1,i,-1):
        if w[i] < w[j]:
            swapvar = j
            break
    #if we wont find swap var and also i got cross limit then it is a last most lexiographic string.
    if swapvar == 0 or i < 0: 
        return "no answer"
    print(i,swapvar)
    ans=""
    for k in range(i):
        ans+=w[k]
    ans+=w[swapvar]
    
    for k in range(n-1,i,-1):
        if swapvar == k:
            ans+=w[i]
        else:
            ans+=w[k]
    return ans
