# https://practice.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1#
# see dhruv goyel solution
# see page no 6 of Journals.
class Solution:
    
    # arr[] : the input array
    # N : size of the array arr[]
    
    #Function to return length of longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self,arr, N):
        s = set()
        c = 1
        maxi = 1
        for i in arr:
            s.add(i)
        for i in arr:
            c=0
            if i-1 not in s:
                
                tmp = i
                # print(tmp)
                while True:
                    if tmp not in s:
                        break
                    tmp+=1
                    c+=1
                maxi = max(maxi , c)
            
        return maxi             
