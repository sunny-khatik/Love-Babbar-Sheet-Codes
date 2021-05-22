# https://practice.geeksforgeeks.org/problems/common-elements1132/1#
#See dhruv goyesls solution
class Solution:
    def commonElements (self, l1,l2,l3, n1, n2, n3):
        # your code here
        ans = list()
        i,j,k=0,0,0
        while i < n1 and j < n2 and k < n3:
            if l1[i] == l2[j] and l2[j] == l3[k]:
                ans.append(l1[i])
                tmp = l1[i]
                while i < n1 and tmp == l1[i]:
                    i+=1
                while j < n2 and tmp == l2[j]:
                    j+=1
                while k < n3 and tmp == l3[k]:
                    k+=1
            elif l1[i] < l2[j]:
                i+=1
            elif l2[j] < l3[k]:
                j+=1
            else:
                k+=1
        return ans
