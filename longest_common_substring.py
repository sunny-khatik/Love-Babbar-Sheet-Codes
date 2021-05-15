class Solution:
    def longestCommonSubstr(self, s1, s2, n, m):
        res=0   #susbstinf kyak pan hoi sake max apde 0 nakhi ne sequance todiye to max no travrse store krvo pade aet;e kaytak be max string hase stoe thase ama
        t = [[0 for i in range(m+1)]for j in range(n+1)]
        for  i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1] == s2[j-1]:
                    t[i][j]=1+t[i-1][j-1]
                    res = max(res , t[i][j])
                else:
                    t[i][j]=0
        return res
