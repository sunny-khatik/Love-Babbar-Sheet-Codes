def getWays(summ, c): #coin array c and summ given in input.
    n = len(c)
    t = [[0 for i in range(summ+1)] for j in range(n+1)]
    for i in range(n+1):
        t[i][0]=1
    for i in range(1,n+1):
        for j in range(1,summ+1):
            if c[i-1] <= j:
                t[i][j] = t[i-1][j] + t[i][j-c[i-1]] #multile time lai sakiye aetle thayi jase
            else:
                t[i][j]=t[i-1][j]
    return t[n][summ]
