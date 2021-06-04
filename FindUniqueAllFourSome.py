# https://practice.geeksforgeeks.org/problems/find-all-four-sum-numbers1732/1#
# See tuf video
class Solution:
    def fourSum(self, a,x):
        n = len(a)
        a.sort()
        i,j=0,1
        ans=list()
        while i < n:
            j = i+1
            while j < n:
                t2 = x-a[i]-a[j]
                start , end= j+1 , n-1
                while start < end:
                    tsum = a[start]+a[end]
                    if tsum < t2:
                        start+=1
                    elif tsum > t2:
                        end-=1
                    else:
                        st,en=a[start] , a[end]
                        ans.append([a[i],a[j],a[start],a[end]])
                        while start < end and a[start] == st:
                            start+=1
                        while start < end and a[end] == en:
                            end-=1
                while j+1 < n and a[j+1] == a[j]:
                    j+=1
                j+=1
            while i+1 < n and a[i+1] == a[i]:
                i+=1
            i+=1
        return ans
