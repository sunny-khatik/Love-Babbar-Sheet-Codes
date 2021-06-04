# https://practice.geeksforgeeks.org/problems/find-missing-and-repeating2512/1#
# see article
class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        rep = -1
        for i in range(n):
            if arr[abs(arr[i])-1] > 0:
                arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
            else:
                rep = abs(arr[i])
        for i in range(n):
            if arr[i] > 0:
                noele = i+1
                break
        return [rep , noele]
